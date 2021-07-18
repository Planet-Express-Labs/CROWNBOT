from discord.ext import commands
from dislash import *
import six
from google.cloud import translate_v2 as translate
import pycountry

from bot import guilds

def translate_text_target(target, text):
    """Translates text into the target language.
    """
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    result = translate_client.translate(text, target_language=target)
    return result['translatedText']


class Translate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @slash_commands.command(name="translate_to",
                            guild_ids=guilds,
                            description="Translates text to a target language.",
                            options=[
                                Option("text", "The text that you want to translate.", type=Type.STRING),
                                Option("language", "The language that you want to translate to.", type=Type.STRING)
                            ])
    async def translate(self, ctx):
        """Translates text to a target language.
        """
        text = ctx.get("text")
        target = ctx.get("language")

        language = pycountry.countries.get(name=target)
        if language is None:
            await ctx.reply("Invalid language.")
            return

        await ctx.reply(type=5)
        translated = translate_text_target(target, text)
        await ctx.edit(translated)


def setup(bot):
    bot.add_cog(Translate(bot))
