import discord
import os

bot = discord.Client()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

bot.run(os.getenv('TOKEN'))