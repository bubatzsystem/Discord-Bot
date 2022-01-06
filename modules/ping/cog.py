import time as t
import nextcord
from nextcord.ext import commands

class Ping(commands.Cog, name="Ping"):
    """Receives ping commands"""
    

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Receives ping commands"""
        ping = nextcord.Embed(description=f"Pong!", color=0x00ff00)

        await ctx.reply(embed=ping, mention_author=True)

def setup(bot: commands.Bot):
    bot.add_cog(Ping(bot))