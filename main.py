import discord
import os
import requests
import json
from riotwatcher import LolWatcher, ApiError

client = discord.Client()

def get_quote():
    response = requests.get()
    json_data = json.loads

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!add'):
        await message.channel.send('Hello')

client.run(os.getenv('TOKEN'))