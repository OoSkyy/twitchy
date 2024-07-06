from discord.ext import tasks
from config import config, twitch_usernames
from twitch import is_user_online
from utils import is_configured

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
            user_status = is_user_online(username)
            currently_online = user_status.get('online')
            stream_url = user_status.get('url', f"https://www.twitch.tv/{username}")
            
            print(f"{username} currently online: {currently_online}, last status: {last_status.get(username)}")
            if currently_online and last_status.get(username) != 'online':
                print(f"Sending online message for {username}")
                await channel.send(f"{username} is online! Watch the stream here: {stream_url}")
                last_status[username] = 'online'
            elif not currently_online and last_status.get(username) != 'offline':
                last_status[username] = 'offline'

    return check_online_status
