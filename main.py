import discord
import keep_alive
from discord.ext import commands
import os
from riotwatcher import LolWatcher, ApiError

bot = commands.Bot(command_prefix='!')
api_key = os.getenv('KEY')
watcher = LolWatcher(api_key)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command(name = 'rank', help = 'type summoner name and region to get rank.i.e. !rank Doublelift na1')
async def rank(ctx, sum_name, region = 'na1'):
    me = watcher.summoner.by_name(region, sum_name)
    my_ranked_stats = watcher.league.by_summoner(region, me['id'])
    if len(my_ranked_stats) == 0:
        await ctx.send("This summoner is unranked!")
    else:
        await ctx.send(
            f"{my_ranked_stats[0]['summonerName']} is {my_ranked_stats[0]['tier']} {my_ranked_stats[0]['rank']}"
        )

keep_alive.keep_alive()
bot.run(os.getenv('TOKEN'))
