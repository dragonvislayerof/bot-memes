import discord
import random
import os
from discord.ext import commands

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'nos hemos logeados como {bot.user}')


@bot.command()
async def mem(ctx):
    try:
        images = os.listdir('images')
        if images:
            img_name = random.choice(images)
# ¡Y así es como se puede sustituir el nombre del fichero desde una variable!
        with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
            await ctx.send(file=picture)

    except FileNotFoundError:
        await ctx.send("¡No se encontraron memes en la carpeta 'imagenes'!")

@bot.command()
async def animales(ctx):
    try:
        images = os.listdir('images')
        if images:
            img_name = random.choice(images)
# ¡Y así es como se puede sustituir el nombre del fichero desde una variable!
        with open(f'animales/{img_name}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
            await ctx.send(file=picture)

    except FileNotFoundError:
        await ctx.send("¡No se encontraron memes en la carpeta 'animales'!")

bot.run("")
