import asyncio
import re

import discord
import random
import logging
from config.bot_config import *
from connectors.connector_common import *
from storage.message_storage import DiscordTrainingDataManager
from common.capture_filter import MessageFilter
from spacy.tokens import Doc


class DiscordReplyGenerator(ConnectorReplyGenerator):
	def generate(self, message: str, doc: Doc = None) -> Optional[str]:

		reply = ConnectorReplyGenerator.generate(self, message, doc, ignore_topics=[BOT_USERNAME.split('#')[0]])

		if reply is None:
			return None

		if DO_REMOVE_PHRASE:
			# Remove bot's username and unwanted words, thanks a lot LeCrankyCoot
			reply = re.sub(BLOCK_PHRASE_ALL, '', reply, flags=re.IGNORECASE)
			reply = re.sub(r' +', ' ', reply)
			reply = reply.strip()

		if DO_REMOVE_URL:
			# Remove URLs
			reply = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', reply)
			reply = re.sub(r' +', ' ', reply)
			reply = reply.strip()

		if len(reply) > 0:
			return reply
		else:
			return None


class DiscordClient(discord.Client):
	def __init__(self, worker: 'DiscordWorker'):
		discord.Client.__init__(self, activity=discord.Game(":3 on the grocery"))
		self._worker = worker
		self._ready = False
		self._logger = logging.getLogger(self.__class__.__name__)

	async def on_ready(self):
		self._ready = True
		self._logger.info(
			"Server join URL: https://discordapp.com/oauth2/authorize?&client_id=%d&scope=bot&permissions=0"
			% CLIENT_ID)

	async def on_message(self, message: discord.Message):

		# Prevent feedback loop
		if str(message.author) == BOT_USERNAME:
			return

		# Ignore certain users
		if str(message.author) in IGNORE_USERS:
			return

		filtered_content = MessageFilter.filter_content(message)

		# Ignore empty messages
		if filtered_content == '':
			return

		learn = False
		# Learn from private messages
		if message.guild is None and LEARN_FROM_DIRECT_MESSAGE:
			DiscordTrainingDataManager().store(message)
			learn = True
		# Learn from all server messages
		elif message.guild is not None and LEARN_FROM_ALL:
			if str(message.channel) not in LEARN_CHANNEL_EXCEPTIONS:
				DiscordTrainingDataManager().store(message)
				learn = True
		# Learn from User
		elif str(message.author) == ALWAYS_LEARN_FROM_USER:
			DiscordTrainingDataManager().store(message)
			learn = True

		# real-time learning
		if learn:
			self._worker.send(ConnectorRecvMessage(filtered_content, learn=True, reply=False))
			self._worker.recv()

		# Reply to mentions
		for mention in message.mentions:
			if str(mention) == BOT_USERNAME:
				self._logger.debug("Message: %s" % filtered_content)
				self._worker.send(ConnectorRecvMessage(filtered_content))
				reply = self._worker.recv()
				if (message.guild.id not in PRIVATE_SERVER_ID or message.guild is None) and DO_REMOVE_PHRASE:
					reply = re.sub(BLOCK_PHRASE_PRIVACY, '', reply, flags=re.IGNORECASE)
					reply = re.sub(r' +', ' ', reply)
					reply = reply.strip()
				if reply.isspace() or reply == '':
					reply = "What?"
				self._logger.debug("Reply: %s" % reply)
				if reply is not None:
					await message.channel.send(reply)
				return

		# Random Reply
		if message.guild is not None and message.guild.id in RANDOM_MESSAGE_SERVER_ID:
			rand = int(random.randint(1, 30))
			if rand == 3:
				self._logger.debug("Message: %s" % filtered_content)
				self._worker.send(ConnectorRecvMessage(filtered_content))
				reply = self._worker.recv()
				if (message.guild.id not in PRIVATE_SERVER_ID) and DO_REMOVE_PHRASE:
					reply = re.sub(BLOCK_PHRASE_PRIVACY, '', reply, flags=re.IGNORECASE)
					reply = re.sub(r' +', ' ', reply)
					reply = reply.strip()
				if reply.isspace() or reply == '':
					reply = "What?"
				self._logger.debug("Reply: %s" % reply)
				if reply is not None:
					await message.channel.send(reply)
			return

		# Reply to private messages
		if message.guild is None:
			self._logger.debug("Private Message: %s" % filtered_content)
			self._worker.send(ConnectorRecvMessage(filtered_content))
			reply = self._worker.recv()
			if DO_REMOVE_PHRASE:
				reply = re.sub(BLOCK_PHRASE_PRIVACY, '', reply, flags=re.IGNORECASE)
				reply = re.sub(r' +', ' ', reply)
				reply = reply.strip()
			if reply.isspace() or reply == '':
				reply = "What?"
			self._logger.debug("Reply: %s" % reply)
			if reply is not None:
				await message.channel.send(reply)
			return


class DiscordWorker(ConnectorWorker):
	def __init__(self, read_queue: Queue, write_queue: Queue, shutdown_event: Event,
	             credentials: DiscordApiCredentials):
		ConnectorWorker.__init__(self, name='DiscordWorker', read_queue=read_queue, write_queue=write_queue,
		                         shutdown_event=shutdown_event)
		self._credentials = credentials
		self._client = None
		self._logger = None

	async def _watchdog(self):
		while True:
			await asyncio.sleep(0.2)

			if self._shutdown_event.is_set():
				self._logger.info("Got shutdown signal.")
				await self._client.close()
				return

	def run(self):
		from storage.message_storage import DiscordTrainingDataManager
		self._logger = logging.getLogger(self.__class__.__name__)
		self._db = DiscordTrainingDataManager()
		self._client = DiscordClient(self)
		self._client.loop.create_task(self._watchdog())
		self._client.run(self._credentials.token)


class DiscordScheduler(ConnectorScheduler):
	def __init__(self, shutdown_event: Event, credentials: DiscordApiCredentials):
		ConnectorScheduler.__init__(self, shutdown_event)
		self._worker = DiscordWorker(read_queue=self._write_queue, write_queue=self._read_queue,
		                             shutdown_event=shutdown_event, credentials=credentials)


class DiscordFrontend(Connector):
	def __init__(self, reply_generator: DiscordReplyGenerator, connectors_event: Event,
	             credentials: DiscordApiCredentials):
		Connector.__init__(self, reply_generator=reply_generator, connectors_event=connectors_event)
		self._scheduler = DiscordScheduler(self._shutdown_event, credentials)