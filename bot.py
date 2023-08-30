import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

import discord
from discord.ext import commands
import logging

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None, application_id=os.environ.get("APP_ID"))

logging.basicConfig(filename="logs/ce_.log", level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

async def load() -> None:
    try:
        for file_name in os.listdir('./cogs'):
            if file_name.endswith(".py") and not file_name.startswith("__"):
                cog_name = file_name[:-3]
                await bot.load_extension(f'cogs.{cog_name}')
    except Exception as e:
        logging.error(f"Errno: cogs installation failed, start again {e}")

async def main() -> None:
    await load()
    try:
        await bot.start(os.environ.get("TOKEN"))
    except Exception as e:
        await bot.close()
        logging.error(f"Errno: The bot fell, it broke, it is closed {e}")