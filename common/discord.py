import discord
import re

from config.discord import *


class DiscordHelper(object):
    @staticmethod
    def filter_content(message: discord.Message):
        # Remove bot mentions from messages
        filtered_content = message.content
        for mention in message.mentions:
            self_id = mention.id
            replace_self = "<@%s>" % self_id
            filtered_content = filtered_content.replace(replace_self, '')
        return filtered_content
