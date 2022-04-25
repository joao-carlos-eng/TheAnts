from discord.ext import commands
from decouple import config

ADMIN = config('admin')
CHANNEL1 = config('channel1')
TOKEN = config("TOKEN")

bot = commands.Bot("NoY-")

bot.run(TOKEN)
