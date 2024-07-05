from discord.ext import tasks
from config import config, twitch_usernames
from twitch import is_user_online
from utils import is_configured

last_status = {}

def setup_tasks(bot):
    @tasks.loop(minutes=5)
    async def check_online_status():
        if not is_configured():
            print("Der Bot ist noch nicht konfiguriert.")
            return
        
        print("Checking online status...")  # Debugging-Ausgabe
        channel = bot.get_channel(config["MESSAGE_CHANNEL_ID"])
        
        for username in twitch_usernames:
            currently_online = is_user_online(username)
            print(f"{username} currently online: {currently_online}, last status: {last_status.get(username)}")  # Debugging-Ausgabe
            if currently_online and last_status.get(username) != 'online':
                print(f"Sending online message for {username}")  # Debugging-Ausgabe
                await channel.send(f"{username} ist online!")
                last_status[username] = 'online'
            elif not currently_online and last_status.get(username) != 'offline':
                last_status[username] = 'offline'
                # Keine Nachricht senden, wenn Benutzer offline ist

    return check_online_status
