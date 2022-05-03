import asyncio

from discord.ext import commands

from noynho.funcoes_auxiliares import consultar_edificio, listar_edificios
from noynho.manager import ADMIN
from noynho.others import elogios, insultos


class Consults(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='consulte')
    async def consult(self, ctx, *expression):
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

    @commands.command(name='edificios')
    async def list_edificios(self, ctx):
        await ctx.send('Estes são os edificios que pode consultar em meu banco de dados:')
        await ctx.send(listar_edificios())

    @commands.command(name='depurar')
    async def depurar(self, ctx, key):
        list = []
        if ctx.author.name == ADMIN:
            if key == 'elogios':
                for elogio in elogios:
                    resp = await ctx.send(f'{elogio}')
                    list.append(resp)

            elif key == 'insultos':
                for insulto in insultos:
                    resp = await ctx.send(f'{insulto}')
                    list.append(resp)

            for x in list:
                await asyncio.sleep(5)
                await x.delete()

            await ctx.send('acabei !!')


def setup(bot):
    bot.add_cog(Consults(bot))
