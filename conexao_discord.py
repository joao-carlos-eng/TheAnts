import discord
from discord.ext import commands, tasks
from funcoes_auxiliares import *
import datetime

bot = commands.Bot("NoY-")

DIAS = [
    'Dia 1: Segunda-feira',
    'Dia 2: Terça-feira',
    'Dia 3: Quarta-feira',
    'Dia 4: Quinta-Feira',
    'Dia 5: Sexta-feira',
    'Dia 6: Sábado',
    'Dia 7: Domingo'
]


@bot.event
async def on_ready():
    print(f'estou pronto !! Estou conectado como {bot.user}')
    acao_da_colonia.start()


@bot.event
async def on_messege(messege):
    if messege.outhor == bot.user:
        return

    await bot.process_commands(messege)


@bot.command(name='oi')
async def send_hello(ctx):
    name = ctx.author.name

    resposta = "Olá, " + name

    await ctx.send(resposta)


@tasks.loop(minutes=5)
async def acao_da_colonia():
    # indice_da_semana = datetime.date.weekday()
    # print(indice_da_semana)

    now = datetime.datetime.now()
    indice_da_semana = now.weekday()
    dia_da_semana = DIAS[indice_da_semana]
    print(dia_da_semana)

    channel = bot.get_channel(957840649841963031)

    await channel.send(now)


bot.run('OTUxNTk1ODI1MDUyNjYzODg5.YipwrA.8xaIdoco00ZF7iD7bE20RjNt3KY')
