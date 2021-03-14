from discord.ext import commands
from dotenv import load_dotenv
from msm.server import *
import os


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 2
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='server', help='Run some server commands')
async def server(ctx, command):
    if command == 'list':        
        await ctx.send(server_list())
        


bot.run(TOKEN)
