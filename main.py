import discord
import os
import asyncio
from discord.ext import commands
import requests
from discord import app_commands

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith(".py"):
            await bot.load_extension(f'cogs.{filename[:-3]}')



async def main():
    await load()
    await bot.start("[TOKEN HERE]")

@bot.event  
async def on_ready():
    print("Bot has connected to Discord.")

asyncio.run(main())
