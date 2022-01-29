# Copyright 2021 Planet Express Labs
# All rights reserved.
# The only reason for taking full copyright is because of a few bad actors.
# As long as you are using my code in good faith, we will probably not have an issue with it.

import discord
from discord.ext import commands
from dislash import *


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_commands.command(
        description="Gets user info",
        options=[
            Option("user", "User to get info for.", type=Type.USER, required=True)
        ],
        name="user-info"
    )
    async def user_info(self, ctx, user=None):
        badges = {
            "staff": "<:staff:812692120049156127>",
            "partner": "<:partner:812692120414322688>",
            "hypesquad": "<:hypesquad_events:812692120358879262>",
            "bug_hunter": "<:bug_hunter:812692120313266176>",
            "hypesquad_bravery": "<:bravery:812692120015339541>",
            "hypesquad_brilliance": "<:brilliance:812692120326373426>",
            "hypesquad_balance": "<:balance:812692120270798878>",
            "verified_bot_developer": "<:verified_bot_developer:812692120133042178>"
        }

        badge_string = ' '.join(badges[pf.name] for pf in user.public_flags.all() if pf.name in badges)
        created_at = str(user.created_at)[:-7]
        reply = discord.Embed(color=discord.Color.blurple())
        reply.title = str(user)
        reply.set_thumbnail(url=user.display_avatar)
        reply.add_field(
            name="Registration",
            value=(
                f"⌚ **Created at:** `{created_at}`\n"
                f"📋 **ID:** `{user.id}`"
            ),
            inline=False
        )
        if len(badge_string) > 1:
            reply.add_field(
                name="Badges",
                value=f"`->` {badge_string}"
            )
        await ctx.reply(embed=reply)

    @commands.has_permissions(manage_messages=True)
    @slash_commands.command(
        name="embed",
        description="Creates an embed",
        options=[
            Option("channel", "Where the message should be sent.", type=Type.CHANNEL),
            Option("title", "Creates a title", type=Type.STRING),
            Option("description", "Creates a description", type=Type.STRING),
            Option("color", "Colors the embed", type=Type.STRING),
            Option("image_url", "URL of the embed's image", type=Type.STRING),
            Option("footer", "Creates a footer", type=Type.STRING),
            Option("footer_url", "URL of the footer image", type=Type.STRING)
        ]
    )
    async def embed(self, ctx, channel=None, title=None, description=None, color=None, image_url=None, footer=None,
                    footer_url=None):
        if color is not None:
            color = await commands.ColorConverter().convert(ctx, color)
        else:
            color = discord.Color.default()
        embed = discord.Embed(color=color)
        if title is not None:
            embed.title = title
        if description is not None:
            embed.description = description
        if image_url is not None:
            embed.set_image(url=image_url)
        footer_args = {}
        if footer is not None:
            footer_args['text'] = footer
        if footer_url is not None:
            footer_args['icon_url'] = footer_url
        if footer_args:
            embed.set_footer(**footer_args)
        if channel is None:
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Sent!")
            await channel.send(embed=embed)

    @commands.has_permissions(ban_members=True)
    @slash_commands.command(
        name="ban",
        description="Ban user",
        options=[
                Option("user", "User to ban", type=Type.USER, required=True),
                Option("purge", "Number of days to purge messages. ", type=Type.INTEGER),
                Option("reason", "Reason for the ban", type=Type.STRING)
                ]
    )
    async def ban(self, ctx, user, reason=None, purge=0):
        try:
            await ctx.guild.ban(user=user, reason=reason, delete_message_days=purge)
            await ctx.reply(f"Success! {user.name} has been banned. ")
        except discord.errors.Forbidden:
            await ctx.reply(f"I do not have permission to execute this command!")

    @commands.has_permissions(manage_messages=True)
    @slash_commands.command(
        name="purge",
        description="Deletes a lot of messages. How many messages? A lot!",
        options=[
            Option("limit", "Number of messages to delete", type=Type.INTEGER, required=True),
            Option("user", "Who's messages to delete", type=Type.USER),
            Option("channel", "Channel from which to delete the messages.", type=Type.CHANNEL)
        ]
    )
    async def purge(self, ctx, limit, user=None, channel=None):
        if channel is None:
            channel = ctx.channel
        messages = []
        if user is None:
            await channel.purge(limit=limit)
        else:
            async for message in channel.history():
                if len(messages) == limit:
                    break
                if message.author == user:
                    messages.append(message)
            await channel.delete_messages(messages)
        await ctx.reply(f"Deleted {limit} messages from {channel.mention}.", ephemeral=True)

    @commands.has_permissions(kick_members=True)
    @slash_commands.command(
        name="kick",
        description="Kick user",
        options=[Option("user", "User to kick", type=Type.USER)]
    )
    async def kick(self, ctx, user):
        try:
            await user.kick()
            await ctx.reply(f"{user.mention} has been kicked successfully.")
        except discord.errors.Forbidden:
            await ctx.reply(f"I do not have permission to execute this command!")


def setup(bot):
    bot.add_cog(Moderation(bot))
