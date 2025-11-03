from discord.ext import commands
import random
from src.utils.db import get_user_balance, update_user_balance

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='rob')
    async def rob(self, ctx, member: commands.MemberConverter):
        if member == ctx.author:
            await ctx.send("Você não pode roubar de si mesmo!")
            return

        target_balance = get_user_balance(member.id)
        if target_balance <= 0:
            await ctx.send(f"{member.mention} não tem 'star coins' para roubar!")
            return

        success = random.choice([True, False])
        if success:
            amount = random.randint(1, target_balance)
            update_user_balance(ctx.author.id, amount)
            update_user_balance(member.id, -amount)
            await ctx.send(f"{ctx.author.mention} roubou {amount} 'star coins' de {member.mention}!")
        else:
            await ctx.send(f"{ctx.author.mention} tentou roubar de {member.mention} e falhou!")

def setup(bot):
    bot.add_cog(Economy(bot))