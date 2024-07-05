# Twitchy Discord Bot

## Overview

Twitchy is a Discord bot that can monitor the online status of Twitch streamers and send notifications in the Discord server when a streamer goes live. The bot also offers commands to add and remove Twitch channels to be monitored, as well as to retrieve information about a Twitch user.

## Prerequisites

- Python 3.x
- Discord Bot Token
- Twitch Client ID and Client Secret

## Installation

### 1. Clone the repository

Clone the repository and change to the directory:

```sh
git clone https://github.com/<your-username>/twitchy.git
cd twitchy
```
### 2. Create and activate a virtual environment

Create a virtual environment and activate it:


```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install dependencies

Install the necessary dependencies:

```sh
pip install -r requirements.txt
```
### 4. Create .env file

Copy the .env.example file to .env

```sh
cp .env.example .env
```
Edit the .env file and add your own values:


```plaintext
DISCORD_TOKEN=your_discord_token_here
TWITCH_CLIENT_ID=your_twitch_client_id_here
TWITCH_CLIENT_SECRET=your_twitch_client_secret_here
```
## Usage

Start the bot:

```sh
python app.py
```
Commands

    !set_command_channel: Sets the current channel as the command channel.
    !set_message_channel: Sets the current channel as the message channel.
    !new_channel <username>: Adds a new Twitch channel to the monitoring list.
    !delete_channel <username>: Removes a Twitch channel from the monitoring list.
    !twitch <username>: Provides information about a Twitch user.

## Example

Set the command channel:

In a Discord channel that you want to set as the command channel:
(Can not be changed afterwards in this version)

    !set_command_channel

Set the message channel:

In a Discord channel where you want to receive notifications:
(Can not be changed afterwards in this version)

    !set_message_channel

Add a Twitch channel:

To add a Twitch channel to the monitoring list:

    !new_channel user_1337

Remove a Twitch channel:

To remove a Twitch channel from the monitoring list:

    !delete_channel user_1337

Get information about a Twitch user:

To get information about a Twitch user:

    !twitch user_1337

## Development

### Folder Structure

```
twitchy/
│
├── app.py
├── config.py
├── twitch.py
├── commands.py
├── tasks.py
├── utils.py
├── .env.example
├── requirements.txt
└── README.md
```

## Description of Files

    app.py: The entry point of the bot. Initializes the bot, loads configurations, and starts the tasks.
    config.py: Contains functions for loading and saving the configuration and channel list.
    twitch.py: Contains functions for communicating with the Twitch API.
    commands.py: Defines the Discord commands.
    tasks.py: Defines the background tasks for checking the online status of Twitch channels.
    utils.py: Contains utility functions.
    .env.example: Example .env file with the necessary environment variables.
    requirements.txt: Contains the required Python packages.
    README.md: This file, which describes the project and provides instructions for installation and usage.

## Developer
### John Klose
