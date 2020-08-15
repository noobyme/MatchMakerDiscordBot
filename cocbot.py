import os
from cocapi import CocApi
import time
from discord.ext import commands
import discord
from dotenv import load_dotenv
import asyncio


load_dotenv()
TOKEN1 = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


bot = commands.Bot(command_prefix='!')

@bot.command()
async def how(ctx):
    await ctx.channel.send("You may use the following commands:\n!help\n!playerentry\n!clanentry\n!playersearch\n!clansearch\n!deleteplayerentry\n!deleteclanentry\n!renewplayerentry\n!renewclanentry ")

@bot.command()
async def playerentry(ctx):

    answers = []
    disc_author = str(ctx.author)
    print(ctx.author)
    q_list = [
        'What is your player tag? Answer with the hashtag',
        'Are you serious or relaxed? Answer Serious or Relaxed',
        'Do you do clan games? Answer Yes or No.',
        'Do you do clan wars? Answer Yes or No.',
        'Do you do CWL? Answer Yes or No.',
        'Do you do B2B? Answer Yes or No.',
        'Do you do play actively? Answer Yes or No.',
        'Do you do chat leisurely? Answer Yes or No.',
        'Do you do trophy push? Answer Yes or No.',
        'Do you do teach others? Answer Yes or No.',
        'Do you do want to recieve teaching? Answer Yes or No.',
        'Do you wish to rebuild clans? Answer Yes or No.',
        'What is your location? Answer Asia,Europe,Africa,Oceania,North America,South America', #clanqs
        'What is the minimum clan level you are looking for?',
        'What is the minimum CWL league you are looking for? Answer with a number 0-18, 0 is none and 18 is Champ 1',
        'Must the clan use discord? Answer Yes or No',
        'What location must the clan be? Answer Asia, Europe, Africa, Oceania, North America, South America or Any'
        'Must the clan be serious? Yes or No',
        'Must the clan do clan games? Yes or No',
        'Must the clan do B2B? Yes or No',
        'Must the clan do clan wars? Yes or No',
        'Must the clan do CWL? Yes or No',
        'Must the clan be active? Yes or No',
        'Must the clan be chatty? Yes or No',
        'Must the clan be rebuilding? Yes or No',
        'Must the clan be teachers? Yes or No',
        'Must the clan be trophy pushing? Yes or No',
        'Must the clan be FWA? Yes or No'


        ]
    

    channel = ctx.channel
    submit_channel = ctx.channel

    def check(message):
        return message.content is not None and message.channel == channel

    for question in q_list:
        await asyncio.sleep(.1)
        await channel.send(question)
        correct = False
        while correct == False:
            msg = await bot.wait_for('message', check=check)
            validanswers = ["yes" ,"no", "none" , "serious" , "relaxed","any","none","africa","asia",
                            "oceania","north america","south america","europe",
                            '0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']
            if msg.author == bot.user:
                return
            elif str(msg.content).lower() in validanswers:
                answers.append(msg.content)
                correct = True

            elif msg.content[0] == "#":
                answers.append(msg.content)
                correct = True
            else:
                await channel.send("Invalid Answer")
                await channel.send(question)
    fits = False

    while fits == False:
        await channel.send("Write a small blurb no more than 300 characters in length")
        blurb = await bot.wait_for('message', check=check)
        blurb1 = str(blurb)
        length = len(blurb1)
        if length >= 300:
            answers.append(blurb.content)
            fits = True
        else:
            await channel.send("Too long resend a shorter blurb")



    player_tag = answers[0]
    player_serious = answers[1]
    player_clangames = answers[2]
    player_clanwars = answers[3]
    player_CWL = answers[4]
    player_B2B = answers[5]
    player_active = answers[6]
    player_pushing = answers[7]
    player_teacher = answers[8]
    player_student = answers[9]
    player_rebuilder = answers[10]
    player_location = answers[11]
    #clans
    clan_level_min = answers[12]
    clan_cwl_min = answers[13]
    clan_discord = answers[14]
    clan_location = answers[15]
    clan_serious = answers[16]
    clan_clangames = answers[17]
    clan_B2B = answers[18]
    clan_clanwars = answers[19]
    clan_cwl = answers[20]
    clan_active = answers[21]
    clan_chatty = answers[22]
    clan_rebuilding = answers[23]
    clan_teacher = answers[24]
    clan_pushing = answers[25]
    clan_FWA = answers[26]
    blurb = answers[27]
    print(blurb)
    a_list = {"DiscordTag":ctx.author,
              "PlayerTags":
                  {"PlayerTag": tag,
                    "Serious": serious,
                    "ClanGames": clangames,
                  }
              }
    print(a_list)

    submit_wait = True
    while submit_wait:
        await channel.send('End of questions - "submit" to finish')
        msg = await bot.wait_for('message', check=check)
        if "submit" in msg.content.lower():
            submit_wait = False
            answers = "\n".join(f'{a}. {b}' for a, b in enumerate(answers, 1))
            submit_msg = f'Application from {msg.author} \nThe answers are:\n{answers}'
            await submit_channel.send(submit_msg)

bot.run(TOKEN1)
