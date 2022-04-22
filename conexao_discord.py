import discord
from discord.ext import commands, tasks

from calendario_acao_da_colonia import DIAS
from funcoes_auxiliares import *
import datetime

bot = commands.Bot("NoY-")


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


    channel = bot.get_channel(957840649841963031)

    await channel.send(now)


bot.run('OTUxNTk1ODI1MDUyNjYzODg5.YipwrA.8xaIdoco00ZF7iD7bE20RjNt3KY')
