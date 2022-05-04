# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
import random

# IMPORT THE OS MODULE.
import os

# IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.
from dotenv import load_dotenv

from discord.ext import commands
import aiohttp

images = os.path.join(os.getcwd(), "Pigs")
client = commands.Bot(command_prefix="!")

# GRAB THE API TOKEN FROM THE .ENV FILE.
DISCORD_TOKEN = 'TOKEN'

def select_random_image_path():
    return os.path.join(images, random.choice(os.listdir(images)))

@client.event
async def on_ready():
	print("Ready")


@client.command()
async def oink(ctx):
	await ctx.send('Oink', file=discord.File(select_random_image_path()))


# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
client.run(DISCORD_TOKEN)
