# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
import random
import os


# IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.
from dotenv import load_dotenv

from discord.ext import commands
import aiohttp

intents = discord.Intents.default()
intents.members = True
images = os.path.join(os.getcwd(), "Pigs")
client = commands.Bot(intents=intents, command_prefix="!")




# GRAB THE API TOKEN FROM THE .ENV FILE.
DISCORD_TOKEN = 'OTcxNDAwNjQ5MDE3MjgyNjIx.YnJ9Wg.pQp2Q_kYWHwwR04GjxQ83686YcI'


def select_random_image_path():
    return os.path.join(images, random.choice(os.listdir(images)))


@client.event
async def on_ready():
    # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
    guild_count = 0


    # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
    for guild in client.guilds:
        # PRINT THE SERVER'S ID AND NAME.
        print(f"- {guild.id} (name: {guild.name})")

        # INCREMENTS THE GUILD COUNTER.
        guild_count = guild_count + 1

    # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
    print("Sebastian The Pig is in " + str(guild_count) + " guilds.")





#!oink at Sebastian for a response
@client.command()
@commands.has_permissions(administrator=True)
async def oink(ctx):
    await ctx.send('Oink', file=discord.File(select_random_image_path()), delete_after=5)


#Send a message to the general channel everytime somebody joins the voice chat
@client.event
async def on_voice_state_update(member, before, after):
    channel = before.channel or after.channel
    userGuild = member.guild

    if channel.id == 477156003498950671: # Insert voice channel ID
        if before.channel is None and after.channel is not None: # Member joins the defined channel
            await userGuild.system_channel.send(member.name + " has entered the Pig Pen") # Send a notification to the channel


# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
client.run(DISCORD_TOKEN)
