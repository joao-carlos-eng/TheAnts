import datetime

from discord.ext import commands


class Smarts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='calcule')
    async def calculate(self, ctx, *expression):
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


def setup(bot):
    bot.add_cog(Smarts(bot))
