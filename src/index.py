import discord
import datetime
import re
from urllib import parse, request
from discord.ext import commands

bot = commands.Bot(command_prefix='/', description="Este es un bot moderador y de ayuda")


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def stats(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}",
                          description="Hola, este es el servidor creado por Santi, diviertanse y respeten las reglas.\n"
                                      "(Para ver las reglas escribir el comando /reglas)",
                          timestamp=datetime.datetime.utcnow(),
                          color=discord.Color.blue())
    embed.add_field(name="Servidor creado el: ", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Dueño del servidor: ", value=f"{ctx.guild.owner}")
    embed.add_field(name="Region del servidor: ", value=f"{ctx.guild.region}")
    embed.add_field(name="ID del servidor; ", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    await ctx.send(embed=embed)


@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}",
                          description="Hola, este es el servidor creado por Santi, diviertanse y respeten las reglas.\n"
                                      "(Para ver las reglas escribir el comando /reglas)",
                          timestamp=datetime.datetime.utcnow(),
                          color=discord.Color.blue())
    embed.add_field(name="Servidor creado el: ", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Dueño del servidor: ", value=f"{ctx.guild.owner}")
    embed.add_field(name="Region del servidor: ", value=f"{ctx.guild.region}")
    embed.add_field(name="ID del servidor; ", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    await ctx.send(embed=embed)


@bot.command()
async def reglas(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}",
                          description="Estas son las reglas del servidor:\n"
                                      "-Prohibido: Insultos raciales, por religión, género, orientación sexual"
                                      " o cualquier otro tipo de discriminación\n"
                                      "-¡Tratense con respeto por favor!\n"
                                      "-Cualquier tópico de discusión esta permitido mientras sea con respeto\n"
                                      "-Esta estrictamente prohibido el spam, sea del contenido que sea.\n"
                                      "-No puede publicitarse mas de una vez a la semana el contenido.\n"
                                      "-¡Recuerden que pueden hacer recomendaciones de lo que gusten!\n"
                                      "-¡Diviertanse!",
                          color=discord.Color.red())
    await ctx.send(embed=embed)


@bot.command()
async def ayuda(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}",
                          description="Algunos de estos comandos pueden ayudarte:\n"
                                      "/ayuda para ver los comandos \n"
                                      "/info para ver información sobre mi, el bot anfitrión y sobre el server \n"
                                      "/stats para ver información sobre mi, el bot anfitrión y sobre el server \n"
                                      "/youtube seguido de lo que quieras para buscarlo en youtube \n"
                                      "/reglas para ver las reglas del server \n"
                                      "/ping para jugar al ping pong conmigo \n"
                                      "/chottomate para ver chotto mate",
                          color=discord.Color.green())
    await ctx.send(embed=embed)


@bot.command()
async def helpme(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}",
                          description="Algunos de estos comandos pueden ayudarte:\n"
                                      "/ayuda para ver los comandos \n"
                                      "/helpme para mas ayuda\n"
                                      "/info para ver información sobre mi, el bot anfitrión y sobre el server \n"
                                      "/stats para ver información sobre mi, el bot anfitrión y sobre el server \n"
                                      "/youtube seguido de lo que quieras para buscarlo en youtube \n"
                                      "/reglas para ver las reglas del server \n"
                                      "/ping para jugar al ping pong conmigo \n"
                                      "/chottomate para ver chotto mate",
                          color=discord.Color.green())
    await ctx.send(embed=embed)


@bot.command()
async def youtube(ctx, *, search):
    query_asked = parse.urlencode({'search_query': search})
    html_result = request.urlopen('https://www.youtube.com/results?' + query_asked)
    search_results = re.findall('/watch\?v=(.{11})', html_result.read().decode())
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])


@bot.command()
async def chottomate(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}",
                          description="Chotto Mate")
    embed.set_thumbnail(url='https://memegenerator.net/img/instances/84812431/chotto-matte.jpg')
    await ctx.send(embed=embed)


# eventos


@bot.event
async def on_ready():
    print("¡Hola, soy un bot y estoy listo para ayudar!")
    await bot.change_presence(activity=discord.Streaming(name="Jugando en streaming a varios juegos!",
                                                         url="https://www.twitch.tv/iamacat95"))


# El bot comienza a trabajar

bot.run('Nzk2NDM4NzczOTczOTA5NTA0.X_X7aA.eYyXH_xtmZtEKMEyjhJq2K8Wx3s')
