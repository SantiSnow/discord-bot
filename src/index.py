
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/', description="Este es un bot moderador y de ayuda")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('Nzk2NDM4NzczOTczOTA5NTA0.X_X7aA.eYyXH_xtmZtEKMEyjhJq2K8Wx3s')
