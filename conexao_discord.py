import time

import discord
from discord.ext import commands, tasks

from calendario_acao_da_colonia import DIAS
from funcoes_auxiliares import *
import datetime

bot = commands.Bot("NoY-")


@bot.event
async def on_ready():
    print(f'estou pronto !! Estou conectado como {bot.user}')
    # acao_da_colonia.start()


conversas = open('conversas.txt', 'w+')


@bot.event
async def on_message(message):
    # print(message.author, message.content)
    conversas.write(message.content)
    if message.author == bot.user and 'destroy' not in message.content:
        return
    if message.content == message.content.upper():
        await message.channel.send(f'por favor {message.author.name}, '
                                   f'não guite com seus colegas.')
    if 'Noynho' in message.content:
        message.channel.send(f'{message.author.name} me chamou ? '
                             f'ainda não entendo muito vocês, mais estou aprendendo :smiling_face_with_tear:')
        message.channel.send(f'então tenham paciencia e se precisarem de algo falem com meu pai.')
    await bot.process_commands(message)

    if message.author == bot.user and 'destroy' in message.content:
        time.sleep(60)

        await message.channel.delete()


@bot.command(name='oi')
async def send_hello(ctx):
    name = ctx.author.name

    resposta = "Olá, " + name

    await ctx.send(resposta)


@tasks.loop(minutes=5)
async def acao_da_colonia():
    channel = bot.get_channel(957840649841963031)

    await channel.send()


@bot.command(name='calcule')
async def calculate(ctx, *expression):
    tipos = ['1m', '5m', '15m', '1h', '3h', '8h']
    minutes = 0
    print(expression)
    for x in expression:
        a, b = x.split('x')
        if 'm' in x:
            minutes += int(a) * int(b.replace('m', ''))
        elif 'h' in x:
            minutes += int(a) * (int(b.replace('h', '')) * 60)

    if minutes == 0:
        print(minutes)
        result = f'ops, acho que errou aí !!\n esses são os tipos aceitos: {tipos}'
    else:
        result = str(datetime.timedelta(seconds=minutes * 60))
        print(result)

    await ctx.send(result)


@bot.command
async def sorry():
    pass


@bot.command(name='consulte')
async def consult(ctx, *expression):
    name, level = '', ''

    if len(expression) == 2:
        name = expression[0]
        level = expression[1]
    elif len(expression) > 2:
        name = " ".join(expression[0:len(expression) - 1])
        level = expression[-1]

    result = consultar_edificio(name, level)

    print(result)
    await ctx.send(result)


bot.run('OTUxNTk1ODI1MDUyNjYzODg5.YipwrA.JOrGfhieueFtpMBmyY96pUrJcfE')
