from typing import ByteString
import discord
from discord import guild
from discord import message
from discord.flags import Intents, MemberCacheFlags
from discord.member import Member
from dotenv import load_dotenv
import os
import aiohttp
import asyncio
import random

memes_random_api = "https://api.chucknorris.io/jokes/random"
memes_search_api = "https://api.chucknorris.io/jokes/search?query="

load_dotenv
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = int(os.getenv("DISCORD_GUILD"))
print(os.getenv("USERNAME"))




intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print ("Estoy listo")
    for guild in client.guilds:
        if guild.id == GUILD:
            for member in guild.members:
                print(member.name)
            break


@client.event
async def on_message(message):
    if message.author == client.user:
        return      

    if message.content.startswith('!hola'):
        await message.channel.send(':last_quarter_moon_with_face: :wine_glass:  :first_quarter_moon_with_face: ')
        return

    if message.content.startswith('!dou'):
        async with aiohttp.ClientSession() as session:
            async with session.get(memes_random_api) as response:
                if response.status == 200:
                    js = await response.json()
                    await message.channel.send(js["value"])
        return

    if message.content.startswith('!search'):
        search_term = message.content[8:]           
        async with aiohttp.ClientSession() as session:
            async with session.get(memes_search_api+search_term) as response:
                if response.status == 200:
                    js = await response.json()
                    await message.channel.send(random.choice(js["result"])["value"])
        return

client.run(TOKEN)



