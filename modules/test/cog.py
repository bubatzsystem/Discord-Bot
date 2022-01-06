import nextcord
from nextcord.ext import commands
from nextcord import Embed
from typing import Optional, Set
from nextcord.ext.commands.core import Group, command



class Test(commands.Cog, name="Test"):
    """This package is a Test Command cog"""
    

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def tcog(self, ctx: commands.Context, command: commands.Command):
        await ctx.send(f"{command.qualified_name}")


    @commands.command()
    async def test(self, ctx: commands.Context):
        """Test Command #1"""
        invite = "https://discord.com/api/oauth2/authorize?client_id=928252355055607869&permissions=8&scope=bot"

        morty = nextcord.Embed(
            description=f"**{ctx.author.mention}** *Just need the Help Menu*\n**Commands**:\n```fix\nDecode Base64: !decode <string> \nEncode Base64: !encode <string> \nPing: !ping \nChoose: !choose <1 2 3>\nRoll: !roll <100d20>```\n**Cogs**:```fix\nRandom: <!roll, !choose>\nPing: <!ping>\nBase64: <!encode, !decode>```",
            color=nextcord.Colour.gold()
        )
        morty.set_author(name="Morty Bot » Help System", url=f"{invite}", icon_url="https://cdn.discordapp.com/attachments/928356816079945839/928632832035794994/morty.jpg")

        await ctx.reply(embed=morty, mention_author=True)

def setup(bot: commands.Bot):
    bot.add_cog(Test(bot))

# embed.set_author(name="Morty Bot » Help System", url="https://discord.com/api/oauth2/authorize?client_id=928252355055607869&permissions=8&scope=bot", icon_url="https://cdn.discordapp.com/attachments/928356816079945839/928632832035794994/morty.jpg")