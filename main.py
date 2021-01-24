import discord
import os
import requests
import json
from discord.ext import commands
from riotwatcher import LolWatcher, ApiError

client = discord.Client()

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def add(ctx):
    if ctx.author == bot.user:
        return

    await ctx.channel.send('Hello')


bot.run(os.getenv('TOKEN'))
