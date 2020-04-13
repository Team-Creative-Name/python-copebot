import discord
import re
from config.bot_config import BLOCK_PHRASE_ALL


class MessageFilter(object):
	@staticmethod
	def filter_content(message: discord.Message):
		filtered_content = message.content
		# Prevents words (declared under bot_config.py) from being captured into the bot's database
		filtered_content = re.sub(BLOCK_PHRASE_ALL, '', filtered_content, flags=re.IGNORECASE)
		# Prevents groups of regional indicator emojis of size 2 or larger from being captured
		# (breaks the bot)
		filtered_content = re.sub(r'([🇦🇧🇨🇩🇪🇫🇬🇭🇮🇯🇰🇱🇲🇳🇴🇵🇶🇷🇸🇹🇺🇻🇼🇽🇾🇿]{2,})', '', filtered_content)
		# Prevents mentions and emails (plus some other things) from being captured
		filtered_content = re.sub(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)|'
		                          r'(<@[!&]?\d+>)|'
		                          r'(<#\d+>)|'
		                          r'(\bowoh\b)|(\bowob\b)', '', filtered_content)
		# Shortens groups of more than one whitespace character to a single whitespace character
		filtered_content = re.sub(r' +', ' ', filtered_content)
		filtered_content = filtered_content.strip()
		return filtered_content
