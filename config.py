import os
import json

CONFIG_FILE = 'config.json'
CHANNELS_FILE = 'channels.json'

config = {
    "COMMAND_CHANNEL_ID": None,
    "MESSAGE_CHANNEL_ID": None
}

# Initialise global variables
twitch_usernames = []
last_status = {}

def load_config():
    global config
    if os.path.isfile(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
        print(f"Loaded config: {config}")

def save_config():
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)
    print("Saved config")

def load_channels():
    global twitch_usernames
    if os.path.isfile(CHANNELS_FILE):
        with open(CHANNELS_FILE, 'r') as f:
            twitch_usernames = json.load(f)
        print(f"Loaded channels: {twitch_usernames}")
    else:
        twitch_usernames = []

def save_channels():
    global twitch_usernames
    with open(CHANNELS_FILE, 'w') as f:
        json.dump(twitch_usernames, f)
    print("Channels saved")

load_config()
load_channels()