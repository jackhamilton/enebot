import discord
from discord.ext import commands

import random
import asyncio
'''
import json
import pprint

import requests
import strawpoll
'''
command_prefix='$'
bot = commands.Bot(command_prefix)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def hello(ctx):
    """Greets the user."""
    await ctx.send("Hello!")
    return

@bot.command()
async def themeidea(ctx, *ideaparts):
    """Adds an idea to the theme list."""
    ideastring = ""
    for idea in ideaparts:
        ideastring += idea + " "
            
    file = open("ideas.txt", "a")
    file.write(ideastring + "\n");
    file.close()
    await ctx.send("Added theme idea to list.")

@bot.command()
async def ideas(ctx):
    """Prints the current list of ideas."""
    file = open("ideas.txt", "r")
    ideas = file.read()
    await ctx.send("Ideas so far:\n")
    await ctx.send(ideas)
    file.close()
"""
@bot.command()
async def themepoll(ctx):
    file = open("ideas.txt", "r")
    ideas = file.read()
    splitideas = ideas.split("\n")
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    url = 'https://strawpoll.me/api/v2/polls' # Set destination URL here
    post_fields = {'title': 'Theme poll: Please pick a theme.', 'options': splitideas, 'multi': 'true'} # Set POST fields here

    request = requests.post(url, data=post_fields, headers=headers)
    print(request.text)
    jsondata = request.json()
    data = json.loads(jsondata)
    pprint.pprint(jsondata)
    await ctx.send("Generated poll! Link: www.strawpoll.me/" + data["id"])
    api = strawpoll.API()
    poll = strawpoll.Poll('Theme poll', splitideas)
    await ctx.send(poll.url)"""
bot.run('NDE5NjI5NTQ3ODQ4MzM1Mzcw.DXy6BA.o8Mu2hx1cv20VQkRwqMkeYOTCzo')
