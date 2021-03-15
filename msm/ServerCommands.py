from discord.ext import commands
import subprocess


class ServerCommands(commands.Cog):
    """Commands to execute MSM's 'server' subcommands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='server', invoke_without_command=True,
            help=' - Commands to manage servers on the Minecraft host')
    async def server(self, ctx):
        await ctx.send('For a list of server commands, run: ```!help server```')


    @server.command(name='list', help=' - List all servers on the Minecraft host')
    async def list_server(self, ctx):
        server_list = subprocess.run(
            ['msm', 'server', 'list'], capture_output=True).stdout.decode('utf-8')
        await ctx.send(server_list)


    @server.command(name='create', help=' - Create a new server on the Minecraft host')
    async def create_server(self, ctx, name: str):
        try:
            await ctx.send('Creating your new Minecraft server, standby...')
            result = subprocess.run(['msm', 'server', 'create', name], check=True)
            # TODO: Add steps to create the eula.txt file and update server.properties
            await ctx.send(f'Your new server named "{name}" is now ready.')
        except subprocess.CalledProcessError as e:
            await ctx.send(f'Uh-oh... {e}')


    @server.command(name='delete', help=' - Deletes a server on the Minecraft host')
    async def delete_server(self, ctx, name: str):
        await ctx.send(f'Deleting your the "{name}"" server on the Minecraft host. Standby...')
        result = subprocess.run(['msm', 'server', 'delete', name], input=b'y')
        await ctx.send(f'"{name}" server has been deleted from the Minecraft host (backups are ' \
                         + 'preserved).')
    
    @server.command(name='rename', help=' - Renames a server on the Minecraft host')
    async def rename_server(self, ctx, current_name: str, new_name: str):
        response = subprocess.check_output(
            ['msm', 'server', 'rename', current_name, new_name]
            ).decode('utf-8')
        await ctx.send(response)


def setup(bot):
    bot.add_cog(ServerCommands(bot))
