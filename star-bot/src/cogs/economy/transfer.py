from discord.ext import commands
from src.utils.db import get_user_balance, update_user_balance

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='transfer')
    async def transfer(self, ctx, member: commands.MemberConverter, amount: int):
        if amount <= 0:
            await ctx.send("Você deve transferir uma quantia positiva de 'star coins'.")
            return

        sender_balance = await get_user_balance(ctx.author.id)
        if sender_balance < amount:
            await ctx.send("Você não tem saldo suficiente para realizar essa transferência.")
            return

        await update_user_balance(ctx.author.id, -amount)
        await update_user_balance(member.id, amount)

        await ctx.send(f"Você transferiu {amount} 'star coins' para {member.mention}.")

def setup(bot):
    bot.add_cog(Economy(bot))