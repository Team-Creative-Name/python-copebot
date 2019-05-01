import discord
from config.discord import *


class DiscordHelper(object):
    @staticmethod
    def filter_content(message: discord.Message):
        # Remove bot mentions from messages or replace mentions with names
        filtered_content = message.content
        for mention in message.mentions:
            if mention.id == DISCORD_USER_ID:
                replace_id = mention.id
                replace_tag = "<@%s>" % replace_id
                filtered_content = filtered_content.replace(replace_tag, '')
            else:
                try:
                    if mention.nick is not None:
                        replace_name = mention.nick
                    else:
                        replace_name = mention.name
                except AttributeError:
                    replace_name = mention.name
                replace_id = mention.id
                replace_tag = "<@%s>" % replace_id
                filtered_content = filtered_content.replace(replace_tag, replace_name)
        return filtered_content
