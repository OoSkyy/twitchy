from discord.ext import tasks
from config import config, twitch_usernames
from twitch import is_user_online
from utils import is_configured
from twitch import get_stream_info
import os
from dotenv import load_dotenv

load_dotenv()

TWITCH_CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")

last_status = {}

def setup_tasks(bot):
    @tasks.loop(minutes=5)
    async def check_online_status():
        if not is_configured():
            print("Twitchy is not configured yet.")
            return
        
        print("Checking online status...")
        channel = bot.get_channel(config["MESSAGE_CHANNEL_ID"])
        
        for username in twitch_usernames:
            stream_info = get_stream_info(username)
            currently_online = is_user_online(username)
            
            if currently_online:
                stream_title = stream_info.get('title', 'Kein Titel verfügbar')
                stream_game = stream_info.get('game', 'Kein Spiel verfügbar')
                stream_url = stream_info.get('url', f"https://www.twitch.tv/{username}")
            
            print(f"{username} currently online: {currently_online}, last status: {last_status.get(username)}")
            
            if currently_online and last_status.get(username) != 'online':
                print(f"Sending online message for {username}")
                await channel.send(
                    f"{username} ist online!\n\n"
                    f"**Title:** {stream_title}\n"
                    f"**Game:** {stream_game}\n"
                    f"Watch here: {stream_url}"
                )
                last_status[username] = 'online'
            elif not currently_online and last_status.get(username) != 'offline':
                last_status[username] = 'offline'

    return check_online_status
