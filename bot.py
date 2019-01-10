import discord
import asyncio
from discord.ext import commands

TOKEN = 'NTMyNjUxMzcyMzI0MTkyMjU2.Dxfp6w.IU8d2caUKh_VyH7TMfcwVu9T3gE'

client = commands.Bot(command_prefix='c!')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------')

@client.event
async def on_message(message):
    if message.content.startswith(command_prefix):
        if message.content.startswith('c!help'):
            if message.content == 'c!help':
                await client.send_message(message.channel,
                    """I'm a calendar bot designed to help you plan and share events!
                       Do `c!help <command>` for more information on a command.
                       Commands:
                       `c!help`
                       `c!create`
                       `c!setstart`
                       `c!setend`
                       `c!delete`
                       `c!finish`""")
            else:
                command_help = message.content[7:]
                if command_help in ['c!help', 'c!create', 'c!setstart', 'c!setend', 'c!delete', 'c!finish']:
                    await client.send_message(message.channel, 'To be implemented')
                else:
                    await client.send_message(message.channel, 'Sorry, this command is not recognized.')
        elif message.content.startswith('c!create'):
            parsed_command = message.content.split('"')
            if len(parsed_command) < 2:
                await client.send_message(message.channel, 'Please specify event name using quotation marks: `c!create "Event Name"`')
            else:
                event_name = parsed_command[1]
                await client.send_message(message.channel, 'Event ' + event_name + ' created')
                
                                          
                   
        

client.run(TOKEN)
