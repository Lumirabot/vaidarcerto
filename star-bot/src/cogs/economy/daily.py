from discord.ext import commands
import random
import datetime
from src.utils.db import get_user_balance, update_user_balance

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='daily')
    async def daily(self, ctx):
        user_id = ctx.author.id
        current_time = datetime.datetime.now()
        last_claim_time = await self.get_last_claim_time(user_id)

        if last_claim_time and (current_time - last_claim_time).days < 1:
            await ctx.send("Você já reivindicou seu prêmio diário hoje!")
            return

        daily_amount = random.randint(50, 100)  # Valor diário aleatório entre 50 e 100
        await update_user_balance(user_id, daily_amount)
        await self.set_last_claim_time(user_id, current_time)

        await ctx.send(f"Você reivindicou {daily_amount} star coins!")

    async def get_last_claim_time(self, user_id):
        # Aqui você deve implementar a lógica para obter o último horário de reivindicação do banco de dados
        pass

    async def set_last_claim_time(self, user_id, claim_time):
        # Aqui você deve implementar a lógica para atualizar o horário da última reivindicação no banco de dados
        pass

def setup(bot):
    bot.add_cog(Economy(bot))