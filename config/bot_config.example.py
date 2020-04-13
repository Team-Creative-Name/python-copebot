class DiscordApiCredentials(object):
    def __init__(self, token: str):
        self.token = token


# --- "User" Stuff Section ---
# ----------------------------

# Discord Application ID
CLIENT_ID = 123456789012345678

# Bot token string
BOT_TOKEN = 'Insert token here'

DISCORD_CREDENTIALS = DiscordApiCredentials(token=BOT_TOKEN)

# Bot username string (in the form 'Username#1111')
BOT_USERNAME = 'Username#1111'

# Bot user ID
SELF_USER_ID = 123456789012345678

# Learn from all servers and channels
LEARN_FROM_ALL = True

# Don't learn from any of these channels (by channel id)
LEARN_CHANNEL_EXCEPTIONS = []

# Learn from direct messages
LEARN_FROM_DIRECT_MESSAGE = True

# Always learn from a specific user no matter what other flags are set
# This should be set to a string containing a username like "SomeGuy#1234"
ALWAYS_LEARN_FROM_USER = None

# Randomly post messages in these servers (by server id)
RANDOM_MESSAGE_SERVER_ID = []

# Allows certain words to be posted in these servers, but not in servers that are not listed on this list
# (useful for privacy) (by server id)
PRIVATE_SERVER_ID = []

# Ignore the following users (use user strings, like 'Username#1111')
IGNORE_USERS = []

# Block the following from being posted and captured everywhere (using regular expressions)
BLOCK_PHRASE_ALL = (r'')

# Block the following to be posted on servers not in PRIVATE_SERVER_ID
BLOCK_PHRASE_PRIVACY = (r'()')

# --- Technical Stuff Section ---
# -------------------------------

# Removes phrases in BLOCK_PHRASE_ALL and BLOCK_PHRASE_PRIVACY
# WARNING! IT IS RECOMMENDED THAT YOU KEEP THIS AS IS FOR YOUR PRIVACY UNLESS YOU DON'T CARE
DO_REMOVE_PHRASE = True

DO_REMOVE_URL = True

# Store training data here
TRAINING_DB_PATH = 'db/discord.db'
