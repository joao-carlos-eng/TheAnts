import datetime
import time

from discord.ext import commands

from bot import ADMIN, CHANNEL1
from calendario_acao_da_colonia import Acao


class Talks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='oi')
    async def send_hello(self, ctx, cnt2=None):
        name = ctx.author.name

        if name == "MalrRy":
            await ctx.send(f"Oiii {name}-Chan")
        elif name == "Morfeu":
            await ctx.send(f'Oi {name}, Gatão !!!')
        elif name == 'patrico' and cnt2 != 0:
            resposta = "Fala chato "
            await ctx.send(resposta)
        elif name == 'patrico' and cnt2 == 0:
            resposta = "Fala Patrick "
            await ctx.send(resposta)
        elif name != ADMIN:
            resposta = "Olá, " + name
            await ctx.send(resposta)
        else:
            await ctx.send('Como vai Mi Lord ?')

    @commands.command(name='acorda')
    async def i_be_back(self, ctx, cnt=None):
        name = ctx.author.name

        if name == "MalrRy":
            await ctx.send('Não estou dormindo, só descançando os olhos nas nuvens')
        elif name == ADMIN:
            await ctx.send('Voltei !!')
        elif name == 'patrico' and cnt == 0:
            cnt += 1
            await ctx.send('fala trolador de bot')

    @commands.command('whoami')
    async def who(self, ctx):
        if ctx.author.name == ADMIN:
            await ctx.send(f'vc é {ctx.author.name} meu criador (aprendi na marra).')
        else:
            return

    @commands.command(name='dormir')
    async def sleep(self, ctx):
        print(ctx.author.name)
        if ctx.author.name == ADMIN:
            await ctx.send('tchau pessoal, tenho que ir, devo ter feito merd@')
            quit()
        else:
            await ctx.send(f'eu te conheço {ctx.author} ?')

    @commands.Cog.listener()
    async def on_message(self, message):
        conversas = open('conversas.txt', 'a+')
        print(message.author, message.content)
        conversas.write(f'{message.content}\n')

        if message.author == self.bot.user and 'destroy' not in message.content:
            return

        if message.content == message.content.upper() and message.content.isalnum() \
                and not message.content.isnum():
            await message.channel.send(f'por favor {message.author.name}, '
                                       f'não guite com seus colegas.')

        if 'noynho'.lower() in message.content.lower() and message.author.name != ADMIN:
            await message.channel.send(f'{message.author.name} me chamou ? '
                                       f'ainda não entendo muito vocês, mais estou aprendendo :smiling_face_with_tear:')

            if message.author.name != ADMIN:
                await message.channel.send(f'então tenham paciencia e se precisarem de algo falem com meu pai.')

        if 'noynho'.lower() in message.content.lower() and message.author.name == ADMIN:
            await message.channel.send(f'oi pai !?')

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
    bot.add_cog(Talks(bot))
