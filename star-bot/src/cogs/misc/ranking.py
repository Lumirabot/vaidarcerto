from discord.ext import commands
from src.utils.db import get_user_balance

class Ranking(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ranking')
    async def ranking(self, ctx):
        """Exibe a classificação dos usuários com base na quantidade de 'star coins'."""
        rankings = await self.get_rankings()
        ranking_message = "Ranking de Star Coins:\n"
        
        for idx, (user_id, balance) in enumerate(rankings, start=1):
            user = self.bot.get_user(user_id)
            username = user.name if user else "Desconhecido"
            ranking_message += f"{idx}. {username}: {balance} star coins\n"
        
        await ctx.send(ranking_message)

    async def get_rankings(self):
        """Obtém a classificação dos usuários do banco de dados."""
        # Aqui você deve implementar a lógica para buscar os dados do banco de dados
        # Exemplo fictício de dados:
        return [
            (1, 100),  # (user_id, balance)
            (2, 80),
            (3, 60),
        ]

def setup(bot):
    bot.add_cog(Ranking(bot))