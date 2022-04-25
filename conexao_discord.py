import time
import discord
from discord.ext import commands, tasks
from decouple import config
from calendario_acao_da_colonia import Acao
from funcoes_auxiliares import *
import datetime

bot = commands.Bot("NoY-")
admin = 'J.C3,14159293'

last_hour = datetime.datetime.now()


@bot.event
async def on_ready():
    print(f'estou pronto !! Estou conectado como {bot.user}')
    acao_da_colonia.start()


cnt2 = 0


@bot.command(name='oi')
async def send_hello(ctx):
    name = ctx.author.name

    if name == "MalrRy":
        await ctx.send(f"Oiii {name}-Chan")
    elif name == "Morfeu":
        await ctx.send(f'Oi {name}, meu Deus grego, Bunitão, Gatão !!!')
    elif name == 'patrico' and cnt2 != 0:
        resposta = "Fala chato "
        await ctx.send(resposta)
    elif name == 'patrico' and cnt2 == 0:
        resposta = "Fala Patrick "
        await ctx.send(resposta)
    elif name != admin:
        resposta = "Olá, " + name
        await ctx.send(resposta)
    else:
        await ctx.send('Como vai Mi Lord ?')


cnt = 0


@bot.command(name='acorda')
async def i_be_back(ctx):
    global cnt
    name = ctx.author.name

    if name == "MalrRy":
        await ctx.send('Não estou dormindo, só descançando os olhos nas nuvens')
    elif name == admin:
        await ctx.send('Voltei !!')
    elif name == 'patrico' and cnt == 0:
        cnt += 1
        await ctx.send('fala trolador de bot')


@tasks.loop(seconds=15)
async def acao_da_colonia():
    global last_hour
    channel = bot.get_channel(963885956593746080)
    now = datetime.datetime.now()

    if now.hour != last_hour:
        last_hour = now.hour
        acao = Acao(now.weekday())
        if now.weekday() == 6:
            prox_dia = Acao(0)
        else:
            prox_dia = Acao(now.weekday() + 1)
        acao.acao(prox_dia)

        if now.minute == 0:
            msg = '\n'.join(acao.message)
            print(msg)
            await channel.send(msg)
        elif now.minute == 30:
            await channel.send(f'Estamos na metade do ação de \"{acao.acao_da_colonia}\"')


@bot.command(name='calcule')
async def calculate(ctx, *expression):
    tipos = ['1m', '5m', '15m', '1h', '3h', '8h']
    minutes = 0
    print(expression)
    try:
        for x in expression:
            a, b = x.split('x')
            if 'm' in x:
                minutes += int(a) * int(b.replace('m', ''))
            elif 'h' in x:
                minutes += int(a) * (int(b.replace('h', '')) * 60)
    except ValueError:
        await ctx.send('opa, vc deve ta querendo me trolar.')
        return

    if minutes == 0:
        print(minutes)
        result = f'ops, acho que errou aí !!\n esses são os tipos aceitos: {tipos}'
    else:
        result = str(datetime.timedelta(seconds=minutes * 60))
        print(result)

    await ctx.send(result)


@bot.command(name='dormir')
async def sleep(ctx):
    print(ctx.author.name)
    if ctx.author.name == admin:
        await ctx.send('tchau pessoal, tenho que ir, devo ter feito merd@')
        quit()
    else:
        await ctx.send(f'eu te conheço {ctx.author} ?')


@bot.command(name='consulte')
async def consult(ctx, *expression):
    name, level = '', ''

    if len(expression) == 2:
        name = expression[0].lower()
        level = expression[1]
    elif len(expression) > 2:
        name = " ".join(expression[0:len(expression) - 1]).lower()
        level = expression[-1]

    result = consultar_edificio(name, level)

    # print(result)
    await ctx.send(result)


@bot.command('whoami')
async def who(ctx):
    if ctx.author.name == admin:
        await ctx.send(f'vc é {ctx.author.name} meu criador (aprendi na marra).')
    else:
        return


conversas = open('conversas.txt', 'a+')


@bot.event
async def on_message(message):
    print(message.author, message.content)
    conversas.write(f'{message.content}\n')

    if message.author == bot.user and 'destroy' not in message.content:
        return
    if message.content == message.content.upper() and message.content.isalnum() \
            and not message.content.isnum():
        await message.channel.send(f'por favor {message.author.name}, '
                                   f'não guite com seus colegas.')
    if 'noynho'.lower() in message.content.lower() and message.author.name != admin:
        await message.channel.send(f'{message.author.name} me chamou ? '
                                   f'ainda não entendo muito vocês, mais estou aprendendo :smiling_face_with_tear:')
        if message.author.name != admin:
            await message.channel.send(f'então tenham paciencia e se precisarem de algo falem com meu pai.')
    if 'noynho'.lower() in message.content.lower() and message.author.name == admin:
        await message.channel.send(f'oi pai !?')
    if "malrry".lower() in message.content.lower():
        await message.send("@MalrRy tão falando de voce :eyes:")
    if message.author == bot.user and 'destroy' in message.content:
        time.sleep(60)
    if "noynho é mentira" in message.content.lower() and message.author.name == admin:
        await message.channel.send("entendido papi, vou ignorar os comando desse usuario")

        await message.channel.delete()

    await bot.process_commands(message)

    if 'qual o próximo ação da colônia' in message.content.lower():
        now = datetime.datetime.now()
        acao = Acao(now.weekday())
        if now.weekday() == 6:
            prox_dia = Acao(0)
        else:
            prox_dia = Acao(now.weekday() + 1)
        acao.hours += 1
        acao.acao(prox_dia)
        channel = bot.get_channel(963885956593746080)

        await channel.send(f'@{message.author}\n {acao.message[1]}')

    if 'qual o ação em andamento' in message.content.lower():
        now = datetime.datetime.now()
        acao = Acao(now.weekday())
        if now.weekday() == 0:
            prox_dia = Acao(0)
        else:
            prox_dia = Acao(now.weekday() + 1)
        acao.acao(prox_dia)
        channel = bot.get_channel(963885956593746080)

        await channel.send(f'@{message.author}\n {acao.message[1]}')


@bot.command(name='edificios')
async def List_edificios(ctx):
    await ctx.send('Estes são os edificios que pode consultar em meu banco de dados:')
    await ctx.send(listar_edificios())


TOKEN = config("TOKEN")
bot.run(TOKEN)
