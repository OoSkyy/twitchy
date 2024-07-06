from discord.ext import commands
from config import config, save_config, twitch_usernames, save_channels, last_status
from twitch import get_twitch_user_info
from utils import is_command_channel, is_configured

def setup_commands(bot):
    @bot.command()
    async def twitch(ctx, *, username: str):
        if not is_configured():
            await ctx.send("Twitchy is not configured yet.")
            return
        
        if not is_command_channel(ctx):
            await ctx.send("you don't have the right oh you don't have the right")
            return
        
        user_info = get_twitch_user_info(username)
        channel = bot.get_channel(config["MESSAGE_CHANNEL_ID"])
        if user_info:
            display_name = user_info.get('display_name', 'N/A')
            description = user_info.get('description', 'N/A')
            view_count = user_info.get('view_count', 'N/A')
            await channel.send(f"User: {display_name}\nDescription: {description}\nView Count: {view_count}")
        else:
            await channel.send(f"No information for user: {username} found.")

    @bot.command()
    async def new_channel(ctx, *, username: str):
        global twitch_usernames, last_status
        if not is_configured():
            await ctx.send("Twitchy is not configured yet.")
            return
        
        if not is_command_channel(ctx):
            await ctx.send("you don't have the right oh you don't have the right")
            return

        username = username.strip()
        if username not in twitch_usernames:
            twitch_usernames.append(username)
            last_status[username] = None  # Initialise status for channel
            save_channels()
            await ctx.send(f"The channel {username} will be stalked.")
        else:
            await ctx.send(f"The channel {username} will be stalked.")

    @bot.command()
    async def delete_channel(ctx, *, username: str):
        global twitch_usernames, last_status
        if not is_configured():
            await ctx.send("Twitchy is not configured yet.")
            return
        
        if not is_command_channel(ctx):
            await ctx.send("you don't have the right oh you don't have the right")
            return

        username = username.strip()
        if username in twitch_usernames:
            twitch_usernames.remove(username)
            last_status.pop(username, None)
            save_channels()
            await ctx.send(f"The channel {username} will not be stalked anymore.")
        else:
            await ctx.send(f"The channel {username} will not be stalked anymore.")

    @bot.command()
    async def set_command_channel(ctx):
        if config["COMMAND_CHANNEL_ID"] is None:
            config["COMMAND_CHANNEL_ID"] = ctx.channel.id
            save_config()
            await ctx.send(f"The command channel was set to {ctx.channel.name}.")
        elif is_command_channel(ctx):
            await ctx.send("The command channel cannot be changed.")
        else:
            await ctx.send("you don't have the right oh you don't have the right")

    @bot.command()
    async def set_message_channel(ctx):
        if config["MESSAGE_CHANNEL_ID"] is None:
            config["MESSAGE_CHANNEL_ID"] = ctx.channel.id
            save_config()
            await ctx.send(f"The message channel was set to {ctx.channel.name}.")
        elif is_command_channel(ctx):
            config["MESSAGE_CHANNEL_ID"] = ctx.channel.id
            save_config()
            await ctx.send(f"The message channel was set to {ctx.channel.name}.")
        else:
            await ctx.send("You cannot change that channel.")
