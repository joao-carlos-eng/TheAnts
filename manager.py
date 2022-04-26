import datetime
import random
import time

import discord
from decouple import config
from others import insultos, saudacao, elogio, elogios
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument, CommandNotFound

from calendario_acao_da_colonia import Acao

CHANNEL = int(config('channel1'))
ADMIN = config('admin')

intents = discord.Intents.default()
intents.members = True


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
        conversas.write(f'{message.author, message.content}\n')

        if message.author == self.bot.user and 'destroy' not in msg:
            return

        if msg == msg.upper() and msg.isalnum() and not msg.isnum():
            await message.channel.send(f'por favor {message.author.name}, não grite.')

        if msg.startswith('noynho') and message.author.name != ADMIN and not any(word in msg for word in insultos)\
                and not any(word in msg for word in elogios):
            await message.channel.send(f'{message.author.name} me chamou ? :eyes:')
        elif msg.startswith('noynho') and message.author.name == ADMIN and not any(word in msg for word in insultos)\
                and not any(word in msg for word in elogios):
            await message.channel.send(f'oi pai')
        elif msg.startswith('noynho') and message.author.name == ADMIN and any(word in msg for word in insultos):
            await message.channel.send(f'maguou :disappointed_relieved:')
        elif msg.startswith('noynho') and any(word in msg for word in insultos):
            await message.channel.send(f'{message.author.name} {random.choice(insultos)}:unamused:')
        elif msg.startswith('noynho') and any(word.lower() in msg.lower() for word in elogios):
            await message.channel.send(f'Obrigado, {message.author.name} '
                                       f'{random.choice(elogio("F" if message.author == "MalrRy" else "M"))}')

        if 'noynho' in msg.lower() and saudacao(msg) and message.author != self.bot.user:
            print(saudacao(msg))
            await message.channel.send(f'{message.author.name}, {saudacao(msg)}:wink:')

        if 'noynho' in msg.lower() and 'desculp' in msg.lower() and message.author != self.bot.user:
            await message.channel.send(f'Tudo bem !! Errar é humano, ainda bem que sou uma maquina :yawning_face:')

        if message.author == self.bot.user and 'destroy' in msg:
            time.sleep(60)
            await msg.channel.delete()

        if "noynho é mentira" in msg.lower() and message.author.name == ADMIN:
            await msg.channel.send("entendido papi, vou ignorar os comando desse usuario")

        if 'noynho vamos aprender ?' in msg.lower() or 'vamos aprender ?' in msg.lower():
            if message.author.name == ADMIN:
                await message.channel.send('Obáh, vamos sim, ligando modo de aprendizagem de maquina.')
            else:
                await message.channel.send('Desculpe ! Você não tem essa permissão.')

        if 'qual o próximo ação da colônia' in msg.lower():
            try:
                now = datetime.datetime.now()
                acao = Acao(now.weekday())
                if now.weekday() == 6:
                    prox_dia = Acao(0)
                else:
                    prox_dia = Acao(now.weekday() + 1)
                acao.hours += 1
                acao.acao(prox_dia)
                channel = self.bot.get_channel(CHANNEL)

                await channel.send(f'@{message.author.name}\n {acao.message[1]}')
            except Exception as erro:
                raise

        if 'qual o ação em andamento' in msg.lower():
            try:
                now = datetime.datetime.now()
                acao = Acao(now.weekday())
                if now.weekday() == 0:
                    prox_dia = Acao(0)
                else:
                    prox_dia = Acao(now.weekday() + 1)
                acao.acao(prox_dia)
                channel = self.bot.get_channel(CHANNEL)

                await channel.send(f'@{msg.author.name}\n {acao.message[1]}')
            except Exception as erro:
                raise


def setup(bot):
    bot.add_cog(Manager(bot))
