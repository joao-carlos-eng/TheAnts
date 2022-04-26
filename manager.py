import datetime
import random
import time
from others import insultos
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument, CommandNotFound

from bot import CHANNEL1, ADMIN
from calendario_acao_da_colonia import Acao


class Manager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'estou pronto !! Estou conectado como {self.bot.user}')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Opa, está faltando algum argumento ai.")
        elif isinstance(error, CommandNotFound):
            await ctx.send('Comando não encontrado.')

    @commands.Cog.listener()
    async def on_message(self, message):
        conversas = open('conversas.txt', 'a+')
        print(message.author, message.content)
        msg = message.content
        conversas.write(f'{msg}\n')

        if message.author == self.bot.user and 'destroy' not in msg:
            return

        if message.content == message.content.upper() and message.content.isalnum() \
                and not message.content.isnum():
            await message.channel.send(f'por favor {message.author.name}, não guite com seus colegas.')

        if message.content.startswith('noynho') and message.author.name != ADMIN:
            await message.channel.send(f'{message.author.name} me chamou ? :yes:')
        elif message.content.startswith('noynho') and message.author.name == ADMIN and not \
                any(word in msg for word in insultos):
            await message.channel.send(f'oi pai !?')
        elif message.content.startswith('noynho') and message.author.name == ADMIN and \
                any(word in msg for word in insultos):
            await message.channel.send(f'maguou :disappointed_relieved:')

        if message.content.startswith('noynho') and any(word in msg for word in insultos):
            await message.channel.send(f'{message.author.name} {random.choice(insultos)}:unamused:')

        if "malrry".lower() in message.content.lower():
            await message.send("@MalrRy tão falando de voce :eyes:")

        if message.author == self.bot.user and 'destroy' in message.content:
            time.sleep(60)

        if "noynho é mentira" in message.content.lower() and message.author.name == ADMIN:
            await message.channel.send("entendido papi, vou ignorar os comando desse usuario")
            await message.channel.delete()

        if 'qual o próximo ação da colônia' in message.content.lower():
            now = datetime.datetime.now()
            acao = Acao(now.weekday())
            if now.weekday() == 6:
                prox_dia = Acao(0)
            else:
                prox_dia = Acao(now.weekday() + 1)
            acao.hours += 1
            acao.acao(prox_dia)
            channel = self.bot.get_channel(CHANNEL1)

            await channel.send(f'@{message.author}\n {acao.message[1]}')

        if 'qual o ação em andamento' in message.content.lower():
            now = datetime.datetime.now()
            acao = Acao(now.weekday())
            if now.weekday() == 0:
                prox_dia = Acao(0)
            else:
                prox_dia = Acao(now.weekday() + 1)
            acao.acao(prox_dia)
            channel = self.bot.get_channel(CHANNEL1)

            await channel.send(f'@{message.author}\n {acao.message[1]}')


def setup(bot):
    bot.add_cog(Manager(bot))
