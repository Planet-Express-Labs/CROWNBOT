import asyncio
import aiohttp
import os
from Weverse.weverseasync import WeverseClientAsync
from CROWNBOT.database import weverse
from discord.ext import commands
from dislash import *

token = os.getenv("crownbot_weverse_token")

web_session = aiohttp.ClientSession()  # A session is created by default
weverse_client = WeverseClientAsync(authorization=token, verbose=True, loop=asyncio.get_event_loop(),
                                    web_session=web_session)


class Weverse(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await weverse_client.start()

    @slash_commands.command(name="subscribe_weverse",
                            description="Sends a message when a subscribed artist does something on Weverse. ",
                            options=[
                                Option("channel", "Where to send subscribed comments"),
                                Option("subscriptions", "Which groups to subscribe to, separate each with a comma.")
                            ])
    async def cmd_subscribe(self, ctx):
        channel = ctx.get("channel")
        subscriptions = ctx.get("subscriptions")




async def setup(bot):
    bot.add_cog(Weverse(bot))
