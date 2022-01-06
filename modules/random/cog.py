import random
from logging import error

import nextcord
from nextcord import colour
from nextcord.ext import commands


class Random(commands.Cog, name="Random"):
    """Returns random results"""
    

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx: commands.Context, dice: str):
        """Returns random results
        
        Example: !roll 2d20
        """
        error = nextcord.Embed(
            description="**Dice must be in the format**: _d_ (*example: 2d6*)",
            color=nextcord.Colour.red()
        )
        try:
            rolls = ""
            total = 0
            amount, die = dice.split("d")
            for _ in range(int(amount)):
                roll = random.randint(1, int(die))
                rolls += f"**{roll}**, "
            rollsem = nextcord.Embed(
                description=f"*Rolls*: {rolls}\n \n*Sum*: **{total}**",
                color=nextcord.Colour.gold()
            )
            await ctx.reply(embed=rollsem)
        except ValueError:
            await ctx.reply(embed=error, mention_author=True)

    @commands.command()
    async def choose(self, ctx: commands.Context, *args):
        """
        ```fix
        Chooses a random item from a list:
        
        Example: !choose "First Option" "Second Option" "Third Option"
        ```
        """
        print(args)
        choice = random.choice(args)
        embed = nextcord.Embed(
            description=f"**{choice}**",
            color=nextcord.Colour.gold()
        )
        await ctx.reply(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Random(bot))
