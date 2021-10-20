import discord
import requests
from discord.ext import commands
import musica
from decouple import config

cogs = [musica]

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot Online!")



for i in range(len(cogs)):
    cogs[i].setup(bot)



TOKEN = config("TOKEN")
bot.run(TOKEN)