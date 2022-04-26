from discord.ext import commands

from funcoes_auxiliares import consultar_edificio, listar_edificios


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


def setup(bot):
    bot.add_cog(Consults(bot))
