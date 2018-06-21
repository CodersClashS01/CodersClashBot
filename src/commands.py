import discord
from discord.ext import commands
import consts


def registerCommands(bot):

    @bot.command(
        pass_context = True, 
        name = "role",
        help = "Add or remove CodersClash-Notify role")
    async def role(ctx):
        msg = ctx.message
        ccrole = [r for r in msg.server.roles if r.id == consts.CCROLEID][0]
        statusstr = ""

        if ccrole in msg.author.roles:
            statusstr = "Removed"
            await bot.remove_roles(msg.author, ccrole)
        else:
            statusstr = "Added"
            await bot.add_roles(msg.author, ccrole)

        await bot.say(embed=discord.Embed(
            description = "%s role <@&%s>." % (statusstr, c.CCROLEID),
            color = c.CLR.DEF ))

    @bot.command(
        pass_context = True, 
        name = "links",
        help = "Display essential links for the event")
    async def links(ctx):
        await bot.say(embed=discord.Embed(
            title = "Essential Links",
            description = """
                \r:white_small_square:   [**Alle Infos**](https://codersclash.de)
                \r:white_small_square:   [**Teamanmeldung**](https://goo.gl/forms/kIHETPs6ObfjYs7J2)
                \r:white_small_square:   [**Teams**](https://github.com/CodersClashS01/Docs/tree/master/teams)
                \r:white_small_square:   [**Requested Dependencies**](https://github.com/CodersClashS01/Docs/blob/master/stuff/requested-dependencies.md)
                """,
            color = c.CLR.DEF ))