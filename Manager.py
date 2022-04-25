from discord.ext import commands


class Manager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print(f'estou pronto !! Estou conectado como {self, bot.user}')



def setup(bot):
    bot.add_cog(Manager(bot))

