import os
from cocapi import CocApi
import time
from discord.ext import commands
import discord
from dotenv import load_dotenv


load_dotenv()
TOKEN1 = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

"""client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

"""
global PlayerList
PlayerList = []
global ClanList
ClanList = []

bot = commands.Bot(command_prefix='!')

@bot.command()
async def playerentry(ctx):
    a_list = {"PlayerTag":"","Serious":"","ClanGames":""}
    q_list = [
        'What is your player tag? Answer with or without the hashtag',
        'Are you serious or relaxed? Answer Serious or Relaxed',
        'Do you do clan games? Answer Yes or No.',
        ]


    channel = await ctx.author.create_dm()
    submit_channel = ctx.channel
    #a = bot.get_channel(736018169696878672)
    #print(a)
    #print(submit_channel)

    """myfile = open("playerlist.txt", "w")
    myfile.write(str(datetime.datetime.now()) + str(chosentags))
    myfile.close()"""

    def check(message):
        return message.content is not None and message.channel == channel

    for question in q_list:
        time.sleep(.5)
        await channel.send(question)
        msg = await bot.wait_for('message', check=check)
        itt = 1
        a_list[1] = msg.content
        itt += 1
        print(a_list)

    submit_wait = True
    while submit_wait:
        await channel.send('End of questions - "submit" to finish')
        msg = await bot.wait_for('message', check=check)
        if "submit" in msg.content.lower():
            submit_wait = False
            answers = "\n".join(f'{a}. {b}' for a, b in enumerate(a_list, 1))
            submit_msg = f'Application from {msg.author} \nThe answers are:\n{answers}'
            await submit_channel.send(submit_msg)

""""@bot.command()
async def clanentry(ctx):
    a_list = []
    q_list = [
        'What is your clan tag?',
        '',
        '']

    channel = await ctx.author.create_dm()
    submit_channel = bot.get_channel(channel)

    def check(message):
        return message.content is not None and message.channel == channel

    for question in q_list:
        time.sleep(.5)
        await channel.send(question)
        msg = await bot.wait_for('message', check=check)
        a_list.append(msg.content)

    submit_wait = True
    while submit_wait:
        await channel.send('End of questions - "submit" to finish')
        msg = await client.wait_for('message', check=check)
        if "submit" in msg.content.lower():
            submit_wait = False
            answers = "\n".join(f'{a}. {b}' for a, b in enumerate(a_list, 1))
            submit_msg = f'Application from {msg.author} \nThe answers are:\n{answers}'
            await submit_channel.send(submit_msg)"""

"""@bot.command()
async def searchclans(ctx):

@bot.command()
async def searchplayers(ctx):

@bot.command()
async def deleteclanentry(ctx):

@bot.command()
async def renewclanentry(ctx):

@bot.command()
async def deleteplayerentry(ctx):

@bot.command()
async def renewplayerentry(ctx):"""

bot.run(TOKEN1)











