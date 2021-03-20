from msm.Configuration import Configuration
from discord.ext import commands
import subprocess

configuration = Configuration()

class ServerCommands(commands.Cog):
    """Commands to execute MSM's 'server' commands."""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(name='server', invoke_without_command=True,
            help=' - Commands to manage servers on the Minecraft host')
    async def server(self, ctx):
        """Parent command for all MSM server management commands"""

        await ctx.send('For a list of server commands, run: ```!help server```')
    
    @server.command(name='start', help=' - Starts the named server')
    async def start_server(self, ctx, server_name: str):
        """Start a Minecraft server"""

        await ctx.send(f'Starting {server_name}. Standby...')
        result = subprocess.run(['msm', server_name, 'start'], check=True)
        print(result)
        await ctx.send(f'Startup process for {server_name} complete. Have fun!')
    
    @server.command(name='stop', help=' - Stops the named server')
    async def stop_server(self, ctx, server_name: str, now=None):
        """Stop a Minecraft server"""

        if now:
            await ctx.send(f'Stopping {server_name} IMMEDIATELY. Standby...')
            result = subprocess.run(['msm', server_name, 'stop', 'now'], check=None)
        else:
            await ctx.send(f'Stopping {server_name}. Standby...')
            result =subprocess.run(['msm', server_name, 'stop'], check=True)
        
        await ctx.send(f'{server_name} is stopped.')
    
    @server.command(name='restart', help=' - Restarts the named server')
    async def restert_server(self, ctx, server_name: str, now=None):
        """Restart a Minecraft server"""
        
        if now:
            await ctx.send(f'Restarting {server_name} IMMDEDIATELY. Standby...')
            result = subprocess.run(['msm', server_name, 'restart', 'now'], check=True)
        else:
            await ctx.send(f'Restarting {server_name}. Standby...')
            result = subprocess.run(['msm', server_name, 'restart'], check=True)
        
        await ctx.send(f'{server_name} has been restarted.')


def setup(bot):
    bot.add_cog(ServerCommands(bot))
