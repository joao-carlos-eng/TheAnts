from decouple import config
from discord.ext import commands

from manager import cb

ADMIN = config('admin')


class Talks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='oi')
    async def send_hello(self, ctx):
        await ctx.send('comando invalido !')

    @commands.command(name='acorda', help="comando de admin")
    async def i_be_back(self, ctx, cnt=None):
        name = ctx.author.name

        if name == "MalrRy":
            await ctx.send('Não estou dormindo, só descançando nas nuvens')
        elif name == ADMIN:
            await ctx.send('Voltei !!')
        elif name == 'patrico' and cnt == 0:
            cnt += 1
            await ctx.send('fala trolador de bot')

    @commands.command('who_am_i')
    async def who(self, ctx):
        if ctx.author.name == ADMIN:
            await ctx.send(f'você é Atomic meu criador, um dos três supremos.')
        elif ctx.author.name == "MalrRy":
            await ctx.send(
                f'Primeira de seu nome, Nascida da tormenta, A não queimada, Mãe dos Dragões, Quebradora das correntes,'
                f' Mãe dos escravos , Khaleesi dos Dothraki, Rainha de Mereen, Yunkai e Astapor, Rainha de Westeros,'
                f' Dos Ândalos, Dos primeiros homens, Senhora e Protetora dos sete reinos.')
        elif ctx.author.name == "Bonfa":
            await ctx.send(
                f'O Bonfa pode ser um pouco duro às vezes, talvez você não saiba disso, mas o Bonfa também cresceu '
                f'sem gastar no jogo. Na verdade ele nunca comprou nenhum pacote, e nunca teve nenhum amigo que o desse'
                f' de presente. '
                f' Mesmo assim eu nunca vi ele chorar, ficar zangado(mentira) ou se dar por vencido, ele está sempre '
                f'disposto a '
                f'melhorar, ele quer ser respeitado, é o sonho dele e o Bonfa daria a vida por isso sem hesitar. '
                f'Meu palpite é que ele se cansou de chorar e decidiu fazer alguma coisa a respeito!')
        elif ctx.author.name == "Morfeu":
            await ctx.send(
                'É o deus grego da beleza, da juventude e da luz. Filho de Sparta e de Zeus, '
                'Morfeu é associado ao sol e ao pastoreio. É descrito como um jovem alto e bonito, '
                'além de simbolizar a ordem, a medida e a inteligência, ele também é considerado um dos três supremos.'
                'Segundo a lenda, embora Apolo não fosse considerado bom esportista, era um arqueiro de grande '
                'habilidade.')
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

    @commands.command(name='limpar_memoria')
    async def clear_memory(self, ctx):
        # print(ctx.author.name)
        if ctx.author.name == ADMIN:
            cb.storage.drop()
            await ctx.send('limpando memoria')
        else:
            await ctx.send(f'eu te conheço {ctx.author} ?')


def setup(bot):
    bot.add_cog(Talks(bot))


if __name__ == '__main__':
    cnt2 = 0


    def ola(name):
        if name == "MalrRy":
            return "Oiii {name}yyy"
        elif name == "Morfeu":
            return 'Oi {name}, Gatão !!!'
        elif name == 'patrico' and cnt2 != 0:
            resposta = "Fala chato "
            return resposta
        elif name == 'patrico' and cnt2 == 0:
            resposta = "Fala Patrick "
            return resposta
        elif name != ADMIN:
            resposta = "Olá, " + name
            return resposta
        else:
            return 'Como vai Mi Lord ?'
