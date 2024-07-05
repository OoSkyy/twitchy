from discord.ext import commands
from config import config, save_config, twitch_usernames, save_channels, last_status
from twitch import get_twitch_user_info
from utils import is_command_channel, is_configured

def setup_commands(bot):
    @bot.command()
    async def twitch(ctx, *, username: str):
        if not is_configured():
            await ctx.send("Der Bot ist noch nicht konfiguriert.")
            return
        
        if not is_command_channel(ctx):
            await ctx.send("Du kannst diesen Befehl nur im dafür vorgesehenen Kanal verwenden.")
            return
        
        user_info = get_twitch_user_info(username)
        channel = bot.get_channel(config["MESSAGE_CHANNEL_ID"])
        if user_info:
            display_name = user_info.get('display_name', 'N/A')
            description = user_info.get('description', 'N/A')
            view_count = user_info.get('view_count', 'N/A')
            await channel.send(f"Benutzer: {display_name}\nBeschreibung: {description}\nView Count: {view_count}")
        else:
            await channel.send(f"Keine Informationen für Benutzer {username} gefunden.")

    @bot.command()
    async def new_channel(ctx, *, username: str):
        global twitch_usernames, last_status
        if not is_configured():
            await ctx.send("Der Bot ist noch nicht konfiguriert.")
            return
        
        if not is_command_channel(ctx):
            await ctx.send("Du kannst diesen Befehl nur im dafür vorgesehenen Kanal verwenden.")
            return

        username = username.strip()
        if username not in twitch_usernames:
            twitch_usernames.append(username)
            last_status[username] = None  # Initialisiere den Status für den neuen Kanal
            save_channels()
            print(f"Der Kanal {username} wurde hinzugefügt. Aktuelle Kanalliste: {twitch_usernames}")  # Debugging-Ausgabe
            await ctx.send(f"Der Kanal {username} wird nun überwacht.")
        else:
            await ctx.send(f"Der Kanal {username} wird bereits überwacht.")

    @bot.command()
    async def delete_channel(ctx, *, username: str):
        global twitch_usernames, last_status
        if not is_configured():
            await ctx.send("Der Bot ist noch nicht konfiguriert.")
            return
        
        if not is_command_channel(ctx):
            await ctx.send("Du kannst diesen Befehl nur im dafür vorgesehenen Kanal verwenden.")
            return

        username = username.strip()
        if username in twitch_usernames:
            twitch_usernames.remove(username)
            last_status.pop(username, None)
            save_channels()
            print(f"Der Kanal {username} wurde entfernt. Aktuelle Kanalliste: {twitch_usernames}")  # Debugging-Ausgabe
            await ctx.send(f"Der Kanal {username} wird nicht mehr überwacht.")
        else:
            await ctx.send(f"Der Kanal {username} wurde nicht gefunden.")

    @bot.command()
    async def set_command_channel(ctx):
        if config["COMMAND_CHANNEL_ID"] is None:
            config["COMMAND_CHANNEL_ID"] = ctx.channel.id
            save_config()
            await ctx.send(f"Der Befehlskanal wurde auf {ctx.channel.name} gesetzt.")
        elif is_command_channel(ctx):
            await ctx.send("Der Befehlskanal ist bereits gesetzt und kann nur in diesem Kanal geändert werden.")
        else:
            await ctx.send("Du kannst den Befehlskanal nur im aktuellen Befehlskanal ändern.")

    @bot.command()
    async def set_message_channel(ctx):
        if config["MESSAGE_CHANNEL_ID"] is None:
            config["MESSAGE_CHANNEL_ID"] = ctx.channel.id
            save_config()
            await ctx.send(f"Der Nachrichtkanal wurde auf {ctx.channel.name} gesetzt.")
        elif is_command_channel(ctx):
            config["MESSAGE_CHANNEL_ID"] = ctx.channel.id
            save_config()
            await ctx.send(f"Der Nachrichtkanal wurde auf {ctx.channel.name} geändert.")
        else:
            await ctx.send("Du kannst den Nachrichtkanal nur im Befehlskanal ändern.")
