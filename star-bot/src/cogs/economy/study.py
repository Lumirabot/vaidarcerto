from discord.ext import commands
import random
from src.utils.db import get_user_balance, update_user_balance

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='study')
    async def study(self, ctx):
        user_id = ctx.author.id
        study_time = random.randint(1, 3)  # Simulate study time in hours
        earnings = study_time * 10  # Earn 10 star coins per hour of study

        # Update user balance in the database
        current_balance = get_user_balance(user_id)
        new_balance = current_balance + earnings
        update_user_balance(user_id, new_balance)

        await ctx.send(f"{ctx.author.mention}, você estudou por {study_time} horas e ganhou {earnings} star coins! Seu novo saldo é {new_balance} star coins.")

def setup(bot):
    bot.add_cog(Economy(bot))