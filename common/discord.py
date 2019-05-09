import discord
import re


class DiscordHelper(object):
    @staticmethod
    def filter_content(message: discord.Message):
        # Remove mentions and emails from messages
        filtered_content = message.content
        filtered_content = re.sub(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)|'
                                  r'(<@!?\d*>)', '', filtered_content)
        filtered_content = filtered_content.strip()
        return filtered_content
