import discord
from discord.ext import commands
import consts


def registerCommands(bot):

    # ------ ROLE COMMAND

    @bot.command(
        pass_context = True, 
        alias = ["r"],
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
            description = "%s role <@&%s>." % (statusstr, consts.CCROLEID),
            color = consts.CLR.DEF ))

    # ------ LINKS COMMAND

    @bot.command(
        pass_context = True, 
        aliases = ["info"],
        name = "links",
        help = "Display essential links for the event")
    async def links(ctx):
        await bot.say(embed = discord.Embed(
            title = "Essential Links",
            description = """
:white_small_square:   [**Alle Infos**](https://codersclash.de)
:white_small_square:   [**Teamanmeldung**](https://goo.gl/forms/kIHETPs6ObfjYs7J2)
:white_small_square:   [**Teams**](https://github.com/CodersClashS01/Docs/tree/master/teams)
:white_small_square:   [**Requested Dependencies**](https://github.com/CodersClashS01/Docs/blob/master/stuff/requested-dependencies.md)
                """,
            color = consts.CLR.DEF ))

    # ------ ORGINV COMMAND

    @bot.command(
        pass_context = True,
        alias = ["org", "githuborg"],
        name = "orginv",
        help = "Sends an mesage to zekro to invite you to the CodersClash organization")
    async def orginv(ctx, *args : str):
        author = ctx.message.author
        if len(args) < 2:
            await bot.say(embed = discord.Embed(
                description = "Please enter your github username / link and yor teams name as arguments!\n" + 
                              "```cc!orginv zekroTJA \"team myteamnotexists\"```",
                color = consts.CLR.ERR ))
        else:
            zekro = await bot.get_user_info(consts.ZEKROID)
            await bot.send_message(zekro, "<@%s> (%s)\n```\n%s\n```" % (author.id, author.id, "\n".join(args)))
            await bot.say(embed = discord.Embed(
                description = ("Your message was send to <@%s> and you will receive an E-Mail or GitHub-Notification " +
                                "as soon as he has invited you to the organization.") % consts.ZEKROID,
                color = consts.CLR.DEF ))