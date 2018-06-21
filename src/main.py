import os

import discord
from discord.ext import commands
import consts
import commands as cmds
import events
import sys


if len(sys.argv) < 2:
    print("Please pass the bots token as first argument!")
    exit(-1)

global CCROLE

bot = commands.Bot(
    command_prefix = consts.PREFIX, 
    description = consts.DESCRIPTION )

events.registerEvents(bot)
cmds.registerCommands(bot)

bot.run(sys.argv[1])