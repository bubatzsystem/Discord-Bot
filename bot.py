import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


def main():
    client = commands.Bot(command_prefix="!")

    load_dotenv()

    @client.event
    async def on_ready():
        print(f"{client.user.name} has connected to Discord.")

    #@client.event
    #async def on_message(ctx):
        #if (ctx.content.startswith("Hello")):
            #await ctx.channel.send(f"Hi {ctx.author.mention}!")

    @client.command()
    async def ping(ctx):
        """Checks for a response from the bot"""
        time = str(round(client.latency * 1000))
        clock = str(round(client.latency * 3000))
        health = str(round(client.latency * 5000))

        ping = discord.Embed(description=f"⌛️ {time}ms\n \n⏱ {clock}ms \n \n💓 {health}ms", color=0x00ff00)

        await ctx.reply(embed=ping, mention_author=True)


    client.run(os.getenv("DISCORD_TOKEN"))

if __name__ == '__main__':
    main()
