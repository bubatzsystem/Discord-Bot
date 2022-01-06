import os

import aiohttp
import nextcord
from nextcord.ext import commands

import config


def main():

    intents = nextcord.Intents.default()
    intents.guilds = True
    intents.members = True

    #activity = nextcord.Activity(type=nextcord.ActivityType.listening, name=f"{config.PREFIX}help")
    bot = commands.Bot(command_prefix=config.PREFIX, intents=intents)


    bot.persistent_views_added = False


    @bot.event
    async def on_ready():
        
        activity_string = 'auf {} servern.'.format(len(bot.guilds))

        print(f"{bot.user.name} has connected to nextcord.")
        await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.playing, name=activity_string))
    
        for folder in os.listdir("modules"):
            if os.path.exists(os.path.join("modules", folder, "cog.py")):
                bot.load_extension(f"modules.{folder}.cog")


    async def startup():
        bot.session = aiohttp.ClientSession()

    bot.loop.create_task(startup())

    bot.run(config.BOT_TOKEN)


if __name__ == '__main__':
    main()
