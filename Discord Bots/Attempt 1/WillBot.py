# bot.py
import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#CHANNEL_ID = os.getenv('CHANNEL_ID')

bot  = commands.Bot(command_prefix="!", intents=discord.Intents.all())



@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Hello! Wills First Bot is ready for action!')
#   channel = bot.get_channel(int())
    #await channel.send("Hello! Study Bot is Ready!")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

bot.run(TOKEN)
