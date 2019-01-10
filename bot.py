import discord
import asyncio
from discord.ext import commands

TOKEN = 'NTMyNjUxMzcyMzI0MTkyMjU2.Dxfp6w.IU8d2caUKh_VyH7TMfcwVu9T3gE'

client = commands.Bot(command_prefix='+cal+')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------')

@client.event
async def on_message(message):
    pass

client.run(TOKEN)
