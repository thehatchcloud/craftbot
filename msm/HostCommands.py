from discord.ext import commands
from datetime import datetime as dt
import subprocess


class HostCommands(commands.Cog):
    """Commands to execute MSM's 'host' server setup subcommands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='host', invoke_without_command=True,
            help=' - Commands to manage setup of the Minecraft host')
    async def host(self, ctx):
        await ctx.send('For a list of server commands, run: ```!help host```')


    @host.command(name='list', help=' - List all servers on the Minecraft host')
    async def list_server(self, ctx):
        server_list = subprocess.run(
            ['msm', 'server', 'list'], capture_output=True).stdout.decode('utf-8')
        await ctx.send(server_list)


    @host.command(name='create', help=' - Create a new server on the Minecraft host')
    async def create_server(self, ctx, name: str):
        try:
            await ctx.send('Creating your new Minecraft server, standby...')
            result = subprocess.run(['msm', 'server', 'create', name], check=True)
            self.agree_to_eula('/opt/msm/servers', name)
            await ctx.send(f'Your new server named "{name}" is now ready.')
        except subprocess.CalledProcessError as e:
            await ctx.send(f'Uh-oh... {e}')


    @host.command(name='delete', help=' - Deletes a server on the Minecraft host')
    async def delete_server(self, ctx, name: str):
        await ctx.send(f'Deleting your the "{name}"" server on the Minecraft host. Standby...')
        result = subprocess.run(['msm', 'server', 'delete', name], input=b'y')
        # TODO: Check if the server exists before trying to delete it.
        await ctx.send(f'"{name}" server has been deleted from the Minecraft host (backups are ' \
                         + 'preserved).')
    
    @host.command(name='rename', help=' - Renames a server on the Minecraft host')
    async def rename_server(self, ctx, current_name: str, new_name: str):
        response = subprocess.check_output(
            ['msm', 'server', 'rename', current_name, new_name]
            ).decode('utf-8')
        await ctx.send(response)
    
    def agree_to_eula(self, msm_server_directory, server_name):
        timestamp = subprocess.run(['date'], capture_output=True).stdout.decode('utf-8').rstrip()
        file_path_name = f'{msm_server_directory}/{server_name}/eula.txt'
        with (open(file_path_name, 'w')) as eula:
            eula.writelines(f'#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).\n#{timestamp}\neula=true')




def setup(bot):
    bot.add_cog(HostCommands(bot))
