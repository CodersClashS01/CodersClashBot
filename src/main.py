import os

import discord
from discord.ext import commands
import consts
import commands as cmds
import events


global CCROLE

bot = commands.Bot(
    command_prefix = consts.PREFIX, 
    description = consts.DESCRIPTION )

events.registerEvents(bot)
cmds.registerCommands(bot)

bot.run(os.environ[consts.TOKENENV])