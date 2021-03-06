from msm.Configuration import Configuration
from msm.CraftBotChecks import check_is_ops_channel
from discord.ext import commands
from datetime import datetime as dt
import subprocess

msm_config = Configuration()

class JarGroupCommands(commands.Cog):
    """Commands to execute MSM's 'jargroup' subcommands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='jargroup', invoke_without_command=True,
            help=' - Commands to manage JarGroups on the Minecraft host')
    async def jargroup(self, ctx):
        """Parent command for all MSM server jargroup commands"""

        await ctx.send('For a list of server commands, run: ```!help jargroup```')

    @jargroup.command(name='list', help=' - List the available JarGroups on the host')
    @commands.check(check_is_ops_channel)
    async def jargroup_list(self, ctx):
        """List available JarGroups on the host"""

        results = subprocess.run(['msm', 'jargroup', 'list'], capture_output=True).stdout.decode('utf-8')
        results = results.rstrip().split('\n')
        results = [x for x in results if not x.startswith(' ')]
        results.sort()
        results = '\n'.join(results)
        response = f'The following Minecraft versions are available on this host:\n\n```\n{results}\n```'
        await ctx.send(response)

def setup(bot):
    bot.add_cog(JarGroupCommands(bot))
