import discord
from discord.ext import commands
import consts


def registerEvents(bot):

    @bot.event
    async def on_ready():
        print("Logged in\nRunning on %d servers.\n\n" 
                % len(bot.servers))
        await bot.change_presence(
            game = discord.Game(name = consts.PREFIX + "help | codersclash.de"))