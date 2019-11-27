import discord
import re
from config.bot_config import BLOCK_PHRASE_ALL


class MessageFilter(object):
	@staticmethod
	def filter_content(message: discord.Message):
		filtered_content = message.content
		# Remove unwanted words from messages
		filtered_content = re.sub(BLOCK_PHRASE_ALL, '', filtered_content, flags=re.IGNORECASE)
		filtered_content = re.sub(r'([🇦🇧🇨🇩🇪🇫🇬🇭🇮🇯🇰🇱🇲🇳🇴🇵🇶🇷🇸🇹🇺🇻🇼🇽🇾🇿]{2,})', '', filtered_content)
		# Remove mentions and emails from messages
		filtered_content = re.sub(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)|'
		                          r'(<@[!&]?\d+>)|'
		                          r'(<#\d+>)|'
		                          r'(\bowoh\b)|(\bowob\b)', '', filtered_content)
		filtered_content = re.sub(r' +', ' ', filtered_content)
		filtered_content = filtered_content.strip()
		return filtered_content
