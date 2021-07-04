# This software is provided free of charge without a warranty.
# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was 
# this file, You can obtain one at https://mozilla.org/MPL/2.0/.
import re
from io import BytesIO

from discord.ext import commands

from cogs.data.confess_db import *
from CROWNBOT.localization import get_string

__version__ = '0.1 PRERELEASE'


def log_confess(ctx, channel, message_object, timestamp):
    embed = discord.Embed(title="Confession made", timestamp=timestamp, description=message_object)
    author = ctx.message.author
    ava_url = author.avatar_url
    embed.set_author(name=author, icon_url=ava_url, url=create_message_link(message_object))
    channel.send(embed=embed)


def create_message_link(guild=None, channel=None, message=None):
    if guild is None:
        guild = message.guild.id
    if channel is None:
        channel = message.channel.id
    message_id = message.id()
    return f"https://discord.com/channels/{guild}/{channel}/{message_id}"


def find_url(url):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s(" \
            r")<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’])) "
    return re.search(url, regex)


async def handle_image_embed(ctx, embed, message):
    files = []
    for file in ctx.message.attachments:
        fp = BytesIO()
        await file.save(fp)
        files.append(discord.File(fp, filename=file.filename, spoiler=file.is_spoiler()))
        image_url = ctx.message.attachments[0].url
        embed.set_image(url=image_url)
        print("image" + image_url)
    image = str(find_url(message))
    if image is not None:
        embed.set_image(url=image)
    return embed


async def send_linked_embed(ctx, link):
    embed = discord.Embed(description=get_string("message_sent"), url=link)
    embed.set_author(name=f"Zoidberg confess v{0}".format(__version__),
                     icon_url="https://i.imgur.com/wWa4zCM.png",
                     url="https://github.com/LiemEldert/ZoidbergBot")
    await ctx.send(embed=embed)


class Confess(commands.Cog):
    """Cog for confessing. As the name makes clear. """

    # noinspection PyShadowingNames
    def __init__(self, bot):
        self.bot = bot

    # @commands.command(name="conf")
    # async def cmd_conf(self, ctx, *, message=""):
    #     if (len(message) != 0) or (ctx.message.attachments != []):
    #         current_time = datetime.now().strftime("%d/%m %H:%M")
    #         user_id = ctx.message.author.id
    #         channel = bot.get_channel(get_db_int("confess_channel", 0))
    #         if get_user_ban(user_id):
    #             await ctx.send(get_string("BANNED_COMMAND"))
    #             pass
    #         # Create embed. They're fancy
    #         embed = discord.Embed(description=f"{message}", timestamp=current_time)
    #         embed = handle_image_embed(ctx, embed, message)
    #         msg = await channel.send(embed=embed)
    #         log_confess(ctx, bot.get_channel(int(LOG_ID)), message, current_time)
    #         await send_linked_embed(ctx, create_message_link(GUILD_ID, channel, msg))
    #     else:
    #         await ctx.send(get_string("COMMAND_EMPTY"))
    #
    # @cmd_conf.error
    # async def conf_error(self, ctx, error):
    #     if isinstance(error, commands.CommandOnCooldown):
    #         await ctx.send('Please wait before sending ')
    #     if isinstance(error, commands.MissingPermissions):
    #         await ctx.send('You do not have manage_messages permission')
    #
    # @commands.command(name="ban-confessions")
    # async def cmd_ban_confessions(self, ctx, *, message=""):
    #     # TODO: convert everything to docstrings.
    #     """Bans a user from using confessions. A reason is not yet supported, but might be implemented soon:tm:.
    #     """
    #     if not verify_user(ctx, "admin"):
    #         await ctx.send(get_string("CMD_PERMISSION_ERROR"))
    #     else:
    #         if message is None:
    #             await ctx.send(get_string("COMMAND_EMPTY_USER_ID"))
    #         else:
    #             add_ban(message)
    #             await ctx.send(f":white_check_mark: Banned {0} from sending confessions.".format(bot.get_user(int(message))))
    #
    # @commands.command(name="unban-confessions", brief="Unbans a user from confessions. ")
    # async def cmd_unban_confessions(self, ctx, *, message=""):
    #     if verify_user(ctx, "admin"):
    #         if message is None:
    #             await ctx.send(
    #                 "Please provide the user ID. To grab someone's ID, enable developer options in appearance, "
    #                 "right click their username and click ''Copy ID''")
    #         else:
    #             try:
    #                 rm_ban(int(message))
    #             except ValueError:
    #                 await ctx.send("Invalid ID. ID must be an integer. ")
    #             await ctx.send("User unbanned from sending confessions. ")
    #             print(f"{ctx.message.author} just unbanned {bot.get_user(int(message))}. ",
    #                   file=open("permissionLog.txt", "a"))
    #     else:
    #         await ctx.send(get_string("CMD_PERMISSION_ERROR"))
    #
    # @commands.command(name="confession-bans", brief="Lists all banned confession users. ")
    # async def cmd_confession_bans(self, ctx):
    #     embed = discord.Embed(description="Getting bans, please wait.")
    #     message = ctx.send(embed=embed)
    #     if verify_user(ctx, "admin"):
    #         if get_bans() is not None:
    #             for each in get_bans():
    #                 embed += "\n {0}".format(bot.get_user(each))
    #                 message.edit(embed=embed)
    #         else:
    #             await ctx.send(get_string("NO_RESULTS"))
    #     else:
    #         await ctx.send(get_string("CMD_PERMISSION_ERROR"))

    @commands.command(name="server_pick_test")
    async def cmd_server_pick_test(self, ctx):
        await ctx.reply(await server_picker(ctx))


def setup(bot):
    bot.add_cog(Confess(bot))
