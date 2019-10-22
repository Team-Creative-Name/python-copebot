import discord
import re
from config.discord import DISCORD_BLOCK_PHRASE


class DiscordHelper(object):
    @staticmethod
    def filter_content(message: discord.Message):
        # Remove mentions and emails from messages
        filtered_content = message.content
        filtered_content = re.sub(DISCORD_BLOCK_PHRASE, '', filtered_content, flags=re.IGNORECASE)
        filtered_content = re.sub(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)|'
                                  r'(<@[!&]?\d+>)|'
                                  r'(<#\d+>)|'
                                  r'(\bowoh\b)|(\bowob\b)', '', filtered_content)
        filtered_content = re.sub(r' +', ' ', filtered_content)
        filtered_content = filtered_content.strip()
        return filtered_content
