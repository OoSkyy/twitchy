import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

from config import save_config, save_channels
#from twitch import get_twitch_token
from commands import setup_commands
from tasks import setup_tasks

# load env variables
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# create intents and configure
intents = discord.Intents.default()
intents.message_content = True  # allow access to messages

# create bot instance
bot = commands.Bot(command_prefix='!', intents=intents)

# event for bot start
@bot.event
async def on_ready():
    print(f'Bot ist eingeloggt als {bot.user.name}')
    if not check_online_status.is_running():
        check_online_status.start()  # start background task

# event for deactivate the bot
@bot.event
async def on_disconnect():
    global twitch_usernames
    save_channels()
    save_config()

# Setup Commands
setup_commands(bot)

# Setup Tasks
check_online_status = setup_tasks(bot)

bot.run(DISCORD_TOKEN)
