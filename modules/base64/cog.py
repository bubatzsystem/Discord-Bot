import base64

import nextcord
from nextcord.ext import commands
from nextcord.ext.commands.core import command

class Base64(commands.Cog, name="Base64"):
    """Base64 decode & encode"""
    

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['e'])
    async def encode(sef, ctx: commands.Context, *, string):
        string_bytes = string.encode("ascii")
        base64_bytes = base64.b64encode(string_bytes) 
        base64_string = base64_bytes.decode("ascii") 

        right = nextcord.Embed(
            description=":white_check_mark:",
            color=nextcord.Colour.gold()
        )
        await ctx.author.send(embed=right)

        embed = nextcord.Embed(
            description=f"*Non encoded*: **{string}** \n*Encoded*: **{base64_string}**",
            color=nextcord.Colour.gold()
        )
        await ctx.reply(embed=embed, mention_author=True)

    @commands.command(aliases=['d'])
    async def decode(self, ctx: commands.Context, *, string):
        string_bytes = string.encode("ascii")
        base64_bytes = base64.b64decode(string_bytes) 
        base64_string = base64_bytes.decode("ascii") 

        right = nextcord.Embed(
            description=":white_check_mark:",
            color=nextcord.Colour.gold()
        )
        await ctx.author.send(embed=right)

        embed = nextcord.Embed(
            description=f"*Non-Decoded*: **{string}** \n*Decoded*: **{base64_string}**",
            color=nextcord.Colour.gold()
        )
        await ctx.send(embed=embed)

        
        
    

def setup(bot: commands.Bot):
    bot.add_cog(Base64(bot))