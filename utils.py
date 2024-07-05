from config import config

def is_command_channel(ctx):
    return ctx.channel.id == config["COMMAND_CHANNEL_ID"]

def is_configured():
    return config["COMMAND_CHANNEL_ID"] is not None and config["MESSAGE_CHANNEL_ID"] is not None
