import discord
import re

from config.discord import *


class DiscordHelper(object):
    @staticmethod
    def filter_content(message: discord.Message):
        # Remove bot mentions from messages
        filtered_content = message.content
        for mention in message.mentions:
            if mention.id == DISCORD_USER_ID:
                self_id = mention.id
                replace_self = "<@%s>" % self_id
                filtered_content = re.sub(replace_self, '', filtered_content)
                filtered_content = filtered_content.strip()
        return filtered_content
