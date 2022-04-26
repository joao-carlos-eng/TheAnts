import datetime
import asyncio
from decouple import config
from discord.ext import commands, tasks
from calendario_acao_da_colonia import Acao

last_hour = datetime.datetime.now()

CHANNEL = int(config('channel1'))


class Tasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = self.bot.get_channel(CHANNEL)
        await channel.send('Eba, me atualizei.')

        self.acao_da_colonia.start()

    @tasks.loop(minutes=1)
    async def acao_da_colonia(self):
        global last_hour
        channel = self.bot.get_channel(CHANNEL)
        now = datetime.datetime.now()

        if now.hour != last_hour or True:
            last_hour = now.hour
            acao = Acao(now.weekday())
            if now.weekday() == 6:
                prox_dia = Acao(0)
            else:
                prox_dia = Acao(now.weekday() + 1)
            acao.acao(prox_dia)

            if now.minute == 0:
                msg = '\n'.join(acao.message)
                resp = await channel.send(msg)
                await asyncio.sleep(59)
                await resp.delete()
            elif now.minute == 30:
                resp = await channel.send(f'Estamos na metade do ação de \"{acao.acao_da_colonia}\"')
                await asyncio.sleep(29*60)
                await resp.delete()
            elif now.minute == 5:
                resp = await channel.send(f'Começou ação da colônia de \"{acao.acao_da_colonia}\"')
                await asyncio.sleep(4 * 60)
                await resp.delete()


def setup(bot):
    bot.add_cog(Tasks(bot))
