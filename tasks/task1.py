import datetime
import asyncio
from decouple import config
from discord.ext import commands, tasks
from pytz import timezone

from calendario_acao_da_colonia import Acao

fuso = timezone('America/Sao_Paulo')
CHANNEL = int(config('channel1'))


class Tasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_acao = None
        self.last_hour = datetime.datetime.now(tz=fuso)

    @commands.Cog.listener()
    async def on_ready(self):
        channel = self.bot.get_channel(CHANNEL)
        #   await channel.send('Eba, me atualizei.')

        self.acao_da_colonia.start()

    @tasks.loop(minutes=1)
    async def acao_da_colonia(self):

        channel = self.bot.get_channel(CHANNEL)
        now = datetime.datetime.now(tz=fuso)

        if now.hour != self.last_hour:
            self.last_hour = now.hour
            self.last_acao = Acao(now.weekday())
            if now.weekday() == 6:
                prox_dia = Acao(0)
            else:
                prox_dia = Acao(now.weekday() + 1)
            self.last_acao.acao(prox_dia)

        acao_da_colonia = self.last_acao.acao_da_colonia
        if now.minute == 0:
            msg = '\n'.join(self.last_acao.message)
            resp = await channel.send(msg)
            await asyncio.sleep(4 * 60)
            await resp.delete()

        elif now.minute == 5:

            resp = await channel.send(f'Começou ação da colônia de \"{acao_da_colonia}\"')
            await asyncio.sleep(25 * 60)
            await resp.delete()

        elif now.minute == 30:

            resp = await channel.send(f'Estamos na metade do ação de \"{acao_da_colonia}\"')
            await asyncio.sleep(29 * 60)
            await resp.delete()

        elif now.minute == 15:

            resp = await channel.send(f'\"{acao_da_colonia}\" acaba em 15min. Fique atento')
            await asyncio.sleep(14 * 60)
            await resp.delete()


def setup(bot):
    bot.add_cog(Tasks(bot))
