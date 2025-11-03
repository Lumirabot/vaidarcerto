from discord.ext import commands
import os

# Initialize the bot with the command prefix
bot = commands.Bot(command_prefix='!')

# Load cogs
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    for filename in os.listdir('./src/cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

# Run the bot with the token from the environment variable
if __name__ == '__main__':
    bot.run(os.getenv('DISCORD_TOKEN'))