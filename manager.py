import asyncio
import datetime
import random
import time
import discord
from decouple import config
from pytz import timezone
from others import saudacao, elogio, elogios, insultar
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument, CommandNotFound
from calendario_acao_da_colonia import Acao

fuso = timezone('America/Sao_Paulo')
hora_atuais = datetime.datetime.now(tz=fuso)

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
        print(message.author, message.content)
        msg = message.content
        chamada1 = msg.lower().startswith('noynho')

        if message.author == self.bot.user and 'destroy' not in msg:
            return

        if str(message.channel.id) != str(CHANNEL):

            if msg == msg.upper() and msg.isalnum() and not msg.isnumeric():
                await message.channel.send(f'por favor {message.author.name}, não grite.')

            if chamada1 and message.author.name != ADMIN and not insultar(msg) \
                    and not any(word.lower() in msg for word in elogios) and not saudacao(msg):
                await message.channel.send(f'{message.author.name} me chamou ? :eyes:')

            elif 'noynho' in msg.lower() and message.author.name != ADMIN and not insultar(msg) \
                    and not any(word.lower() in msg for word in elogios) and not saudacao(msg):
                await message.channel.send(f'{message.author.name} está falando de mim ? :eyes:')

            elif chamada1 and message.author.name == ADMIN and not insultar(msg) \
                    and not any(word.lower() in msg.lower() for word in elogios):
                await message.channel.send(f'oi pai')

            elif chamada1 and message.author.name == ADMIN and insultar(msg):
                await message.channel.send(f'maguou :disappointed_relieved:')

            elif chamada1 and insultar(msg):
                palavra = insultar(msg)
                if message.author.name == 'MalrRy':
                    palavra = insultar(msg, pronome='F')
                await message.channel.send(f'E você {message.author.name} é {palavra} :unamused:')

            elif chamada1 and any(word.lower() in msg.lower() for word in elogios):
                await message.channel.send(f'Obrigado, {message.author.name} você é '
                                           f'{random.choice(elogio("F" if message.author.name == "MalrRy" else "M"))}')

            if 'noynho' in msg.lower() and saudacao(msg) and message.author != self.bot.user:
                await message.channel.send(f'{message.author.name}, {saudacao(msg)}:wink:')

            if 'noynho' in msg.lower() and 'desculp' in msg.lower() and message.author != self.bot.user:
                await message.channel.send(f'Tudo bem !! Errar é humano, ainda bem que sou uma maquina :yawning_face:')

            if message.author == self.bot.user and 'destroy' in msg:
                time.sleep(60)
                await msg.channel.delete()

            if "noynho é mentira" in msg.lower() and message.author.name == ADMIN:
                await msg.channel.send("entendido papi, vou ignorar os comando desse usuario")

            if 'noynho vamos aprender' in msg.lower() or 'vamos aprender ?' in msg.lower():
                if message.author.name == ADMIN:
                    await message.channel.send('Obáh, vamos sim, ligando modo de aprendizagem de maquina.')
                else:
                    await message.channel.send('Desculpe ! Você não tem essa permissão.')

            if 'qual o próximo ação da colônia' in msg.lower():

                now = datetime.datetime.now(tz=fuso)
                acao = Acao(now.weekday())
                if now.weekday() == 6:
                    prox_dia = Acao(0)
                else:
                    prox_dia = Acao(now.weekday() + 1)
                acao.hours += 1
                acao.acao(prox_dia)
                channel = self.bot.get_channel(CHANNEL)

                await channel.send(f'<@{message.author.id}>\n{acao.message[1]}')

            elif 'qual o ação em andamento' in msg.lower():
                now = datetime.datetime.now(tz=fuso)
                acao = Acao(now.weekday())
                if now.weekday() == 0:
                    prox_dia = Acao(0)
                else:
                    prox_dia = Acao(now.weekday() + 1)
                acao.acao(prox_dia)
                channel = self.bot.get_channel(CHANNEL)

                await channel.send(f'<@{message.author.id}>\n {acao.message[1]}')
        else:
            if 'qual o próximo ação da colônia' in msg.lower():

                now = datetime.datetime.now(tz=fuso)
                acao = Acao(now.weekday())
                if now.weekday() == 6:
                    prox_dia = Acao(0)
                else:
                    prox_dia = Acao(now.weekday() + 1)
                acao.hours += 1
                acao.acao(prox_dia)
                channel = self.bot.get_channel(CHANNEL)

                await channel.send(f'<@{message.author.id}>\n{acao.message[1]}')

            elif 'qual o ação em andamento' in msg.lower():
                now = datetime.datetime.now(tz=fuso)
                acao = Acao(now.weekday())
                if now.weekday() == 0:
                    prox_dia = Acao(0)
                else:
                    prox_dia = Acao(now.weekday() + 1)
                acao.acao(prox_dia)
                channel = self.bot.get_channel(CHANNEL)

                await channel.send(f'@<{message.author.id}>\n {acao.message[1]}')
            else:

                autor = message.author.id
                msg2 = await message.channel.send(
                    f'<@{autor}> por favor, evite assuntos paralelos nesse canal.\n'
                    f'Para conversas aleatórias se diriga a algum dos \'burburinhos\'')
                await asyncio.sleep(5)
                await msg2.delete()
                await message.delete()


def setup(bot):
    bot.add_cog(Manager(bot))
