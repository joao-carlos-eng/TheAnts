import os
from discord.ext import commands
from decouple import config

ADMIN = config('admin')
CHANNEL1 = config('channel1')
TOKEN = config("TOKEN")

bot = commands.Bot("NoY-")


def load_cog(bot):
    bot.load_extension('manager')
    bot.load_extension('tasks.task1')
    for file in os.listdir('commands'):

        if file.endswith('.py'):
            cog = file[:-3]
            bot.load_extension(f'commands.{cog}')


load_cog(bot)

bot.run(TOKEN)
