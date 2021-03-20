from msm.Configuration import Configuration
from discord.ext import commands
from datetime import datetime as dt
import subprocess

msm_config = Configuration()

class HostCommands(commands.Cog):
    """Commands to execute MSM's 'host' server setup subcommands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='host', invoke_without_command=True,
            help=' - Commands to manage setup of the Minecraft host')
    async def host(self, ctx):
        """Parent command for all MSM server host setup commands"""

        await ctx.send('For a list of server commands, run: ```!help host```')


    @host.command(name='list', help=' - List all servers on the Minecraft host')
    async def list_server(self, ctx):
        """List all Minecraft servers on the host."""

        server_list = subprocess.run(
            ['msm', 'server', 'list'], capture_output=True).stdout.decode('utf-8')
        await ctx.send(server_list)


    @host.command(name='create', help=' - Create a new server on the Minecraft host')
    async def create_server(self, ctx, name: str):
        """Create a new Minecraft server on the host"""

        try:
            await ctx.send('Creating your new Minecraft server, standby...')
            result = subprocess.run(['msm', 'server', 'create', name], check=True)
            self.agree_to_eula(msm_config.settings['SERVER_STORAGE_PATH'], name)
            # TODO: Add the step to change the jargroup to spigot server
            # TODO: Create the default server property file
            await ctx.send(f'Your new server named "{name}" is now ready.')
        except subprocess.CalledProcessError as e:
            await ctx.send(f'Uh-oh... {e}')


    @host.command(name='delete', help=' - Deletes a server on the Minecraft host')
    async def delete_server(self, ctx, name: str):
        """Delete a Minecraft server on the host"""

        await ctx.send(f'Deleting your the "{name}"" server on the Minecraft host. Standby...')
        result = subprocess.run(['msm', 'server', 'delete', name], input=b'y')
        # TODO: Check if the server exists before trying to delete it.
        await ctx.send(f'"{name}" server has been deleted from the Minecraft host (backups are ' \
                         + 'preserved).')
    
    @host.command(name='rename', help=' - Renames a server on the Minecraft host')
    async def rename_server(self, ctx, current_name: str, new_name: str):
        """Rename a Minecraft server on the host"""

        response = subprocess.check_output(
            ['msm', 'server', 'rename', current_name, new_name]
            ).decode('utf-8')
        await ctx.send(response)
    
    def agree_to_eula(self, msm_server_directory, server_name):
        """Create the eula.txt file to show agreement with Mojang's EULA."""

        timestamp = subprocess.run(['date'], capture_output=True).stdout.decode('utf-8').rstrip()
        file_path_name = f'{msm_server_directory}/{server_name}/eula.txt'
        with (open(file_path_name, 'w')) as eula:
            eula.writelines(f'#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).\n#{timestamp}\neula=true')
    
    def create_default_server_settings_file(self, msm_server_directory, server_name, version_number):
        """Create the default server.properties file with the server version included"""
        
        default_properties = msm_config.default_server_properties
        default_properties['msm-version'] = version_number
        default_properties['motd'] = f'Autism Up - {server_name} session'
        timestamp = subprocess.run(['date'], capture_output=True).stdout.decode('utf-8').rstrip()

        with (open(f'{msm_server_directory}/{server_name}/server.properties', 'w')) as properties:
            properties.write('#Minecraft server properties')
            properties.write(f'#{timestamp}')
            for key, value in default_properties.items():
                properties.write(f'{property[key]}={property[item]}')


def setup(bot):
    bot.add_cog(HostCommands(bot))