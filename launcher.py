from lib.bot import bot
import os

VERSION = "0.0.1"
TOKEN = os.environ.get("DISCORD_TOKEN")

bot.run(VERSION, TOKEN)
