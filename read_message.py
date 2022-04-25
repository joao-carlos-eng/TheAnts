import datetime
import time

from calendario_acao_da_colonia import Acao
from conexao_discord import bot, admin

conversas = open('conversas.txt', 'a+', encoding='utf-8')


async def on_message(message):
    print(message.author, message.content)
    conversas.write(message.content)

    if message.author == bot.user and 'destroy' not in message.content:
        return
    if message.content == message.content.upper() and message.content.isalnum():
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

    if 'qual o proximo acao da colonia ?' in message.content.lower():
        now = datetime.datetime.now()
        acao = Acao(now.weekday())
        acao.hours += 1
        acao.acao()
        channel = bot.get_channel(957840649841963031)

        await channel.send(f'{message.author.name}\n {acao.message[1]}')
