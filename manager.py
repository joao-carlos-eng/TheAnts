import datetime
import random
import time
import discord
from decouple import config
from pytz import timezone
from Users.UsuariosDiscord import Players
from chatbot.chatbot import *
from conexao_fire_base import get
from others import insultos, saudacao, elogio, elogios
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
        self.data = None
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.data = {}
        print(f'estou pronto !! Estou conectado como {self.bot.user}')
        canal = self.bot.get_guild()
        await canal.send(':eyes:')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Opa, está faltando algum argumento ai.")
        elif isinstance(error, CommandNotFound):
            await ctx.send('Comando não encontrado.')

    @commands.Cog.listener()
    async def on_message(self, message):
        # list_players = get('Players').values()
        # if message.author.name not in [x['nickDiscord'].lower() for x in list_players] and \
        #         message.guild == 'Servidor de desenvolvimento':
        #     player = Players(message.author.id)
        #     player.criar()

        print(message.author, message.content)
        msg = message.content
        chamada1 = msg.lower().startswith('noynho')
        # conversas.write(f'{message.author, message.content}\n')

        if message.author == self.bot.user and 'destroy' not in msg:
            return

        if msg == msg.upper() and msg.isalnum() and not msg.isnumeric():
            await message.channel.send(f'por favor {message.author.name}, não grite.')

        if chamada1 and message.author.name != ADMIN and not any(word.lower() in msg.lower() for word in insultos) \
                and not any(word.lower() in msg for word in elogios) and not saudacao(msg):
            await message.channel.send(f'{message.author.name} me chamou ? :eyes:')

        # elif chamada1 and message.author.name == ADMIN and not any(word.lower() in msg.lower() for word in insultos) \
        #         and not any(word.lower() in msg.lower() for word in elogios):
        #     await message.channel.send(f'oi pai')

        elif chamada1 and message.author.name == ADMIN and any(word.lower() in msg.lower() for word in insultos):
            print()
            await message.channel.send(f'maguou :disappointed_relieved:')

        elif chamada1 and any(word.lower() == msg.lower() for word in insultos):
            palavra_sorteada = random.choice(insultos)
            if message.author.name == 'MalrRy' and palavra_sorteada.endswith('o'):
                palavra_sorteada.pop()
                palavra_sorteada += 'a'
            await message.channel.send(f'E você {message.author.name} é {palavra_sorteada} :unamused:')

        elif chamada1 and any(word.lower() in msg.lower() for word in elogios):
            await message.channel.send(f'Obrigado, {message.author.name} você é '
                                       f'{random.choice(elogio("F" if message.author.name == "MalrRy" else "M"))}')
        elif chamada1 and not any(word.lower() in msg.lower() for word in insultos) \
                and not any(word.lower() in msg.lower() for word in elogios) and not saudacao(msg):
            ky = message.author.name.lower() + " ~ " + msg
            resp = chatbot.get_response(ky)
            print(msg)
            if float(resp.confidence) > 0.2:
                print("Noynho: ", resp)
                await message.channel.send(resp)
            else:
                await message.channel.send("Não entendi :(")
                print("Não entendi :(")

        if 'noynho' in msg.lower() and saudacao(msg) and message.author != self.bot.user:
            await message.channel.send(f'{message.author.name}, {saudacao(msg)} :wink:')

        if 'noynho' in msg.lower() and 'desculp' in msg.lower() and message.author != self.bot.user:
            await message.channel.send(f'Tudo bem !! Errar é humano, ainda bem que sou uma maquina :yawning_face:')

        if message.author == self.bot.user and 'destroy' in msg:
            time.sleep(60)
            await message.channel.delete()

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

            await channel.send(f'@{message.author.name}\n{acao.message[1]}')

        elif 'qual o ação em andamento' in msg.lower():
            now = datetime.datetime.now(tz=fuso)
            acao = Acao(now.weekday())
            if now.weekday() == 0:
                prox_dia = Acao(0)
            else:
                prox_dia = Acao(now.weekday() + 1)
            acao.acao(prox_dia)
            channel = self.bot.get_channel(CHANNEL)

            await channel.send(f'@{message.author.name}\n {acao.message[1]}')


def setup(bot):
    bot.add_cog(Manager(bot))
