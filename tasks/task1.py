import datetime
from discord.ext import commands, tasks
from bot import CHANNEL1
from calendario_acao_da_colonia import Acao

last_hour = datetime.datetime.now()


class Tasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.acao_da_colonia.start()

    @tasks.loop(seconds=15)
    async def acao_da_colonia(self):
        global last_hour
        channel = self.bot.get_channel(CHANNEL1)
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


def setup(bot):
    bot.add_cog(Tasks(bot))
