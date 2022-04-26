from decouple import config
from discord.ext import commands

ADMIN = config('admin')


class Talks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='oi')
    async def send_hello(self, ctx, cnt2=None):
        name = ctx.author.name

        if name == "MalrRy":
            await ctx.send(f"Oiii {name}-Chan")
        elif name == "Morfeu":
            await ctx.send(f'Oi {name}, Gatão !!!')
        elif name == 'patrico' and cnt2 != 0:
            resposta = "Fala chato "
            await ctx.send(resposta)
        elif name == 'patrico' and cnt2 == 0:
            resposta = "Fala Patrick "
            await ctx.send(resposta)
        elif name != ADMIN:
            resposta = "Olá, " + name
            await ctx.send(resposta)
        else:
            await ctx.send('Como vai Mi Lord ?')

    @commands.command(name='acorda')
    async def i_be_back(self, ctx, cnt=None):
        name = ctx.author.name

        if name == "MalrRy":
            await ctx.send('Não estou dormindo, só descançando os olhos nas nuvens')
        elif name == ADMIN:
            await ctx.send('Voltei !!')
        elif name == 'patrico' and cnt == 0:
            cnt += 1
            await ctx.send('fala trolador de bot')

    @commands.command('whoami')
    async def who(self, ctx):
        if ctx.author.name == ADMIN:
            await ctx.send(f'vc é {ctx.author.name} meu criador (aprendi na marra).')
        else:
            return

    @commands.command(name='dormir')
    async def sleep(self, ctx):
        print(ctx.author.name)
        if ctx.author.name == ADMIN:
            await ctx.send('tchau pessoal, tenho que ir, devo ter feito merd@')
            quit()
        else:
            await ctx.send(f'eu te conheço {ctx.author} ?')


def setup(bot):
    bot.add_cog(Talks(bot))
