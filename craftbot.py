from discord.ext import commands
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

extensions = [
    'msm.HostCommands',
    'msm.ServerCommands',
]

for extension in extensions:
    bot.load_extension(extension)


bot.run(TOKEN)
