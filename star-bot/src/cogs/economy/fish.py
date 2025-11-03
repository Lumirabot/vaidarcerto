from discord.ext import commands
import random

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='fish')
    async def fish(self, ctx):
        """Permite aos usuários pescar e ganhar 'star coins'."""
        catch = random.choice(['peixe', 'nada'])
        if catch == 'peixe':
            earnings = random.randint(1, 10)  # Ganho aleatório de 1 a 10 star coins
            await ctx.send(f"{ctx.author.mention} você pescou um peixe e ganhou {earnings} star coins!")
            # Aqui você deve adicionar a lógica para atualizar o saldo do usuário no banco de dados
        else:
            await ctx.send(f"{ctx.author.mention} você não pegou nada desta vez.")

def setup(bot):
    bot.add_cog(Economy(bot))