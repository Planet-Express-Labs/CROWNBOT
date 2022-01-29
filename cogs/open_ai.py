# Copyright 2021 Planet Express Labs
# All rights reserved.
# The only reason for taking full copyright is because of a few bad actors.
# As long as you are using my code in good faith, we will probably not have an issue with it.

# Copyright 2021 Planet Express Labs
# All rights reserved.
# The only reason for taking full copyright is because of a few bad actors.
# As long as you are using my code in good faith, we will probably not have an issue with it.
from typing import Text
import openai
from discord.ext import commands
from dislash import *


async def gpt_3_correct(ctx, text: Text):
    """
    Cleans gramatical errors in the text, but using gpt-3. 
    :Context ctx:
    """
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Original: {text}\nStandard American English:",
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    await ctx.reply(response.choices[0].text)


class OpenAI(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # @commands.slash_command(name="explain-code", brief="Explains complicated code using AI")
    # async def cmd_explain_code(self, ctx, code: str = commands.Param()):
    #     """
    #     Explains complicated code using AI
    #     :Context ctx:
    #     :string code:
    #     """
    #     response = openai.Completion.create(
    #         engine="davinci-codex",
    #         prompt=code + "Here's what the above class is doing:\n1.",
    #         temperature=0,
    #         max_tokens=64,
    #         top_p=1.0,
    #         frequency_penalty=0.0,
    #         presence_penalty=0.0,
    #         stop=["\"\"\""]
    #     )
    #     await ctx.response.send_message(response.choices[0].text)

    @slash_commands.command(name="gpt3_correct",
                            description="Clears grammatical errors in the input text using gpt-3",
                            options=[
                                Option("text", "Text to correct", type=Type.STRING)
                            ]
                            )
    async def cmd_gpt3_correct(self, ctx):
        text = ctx.get("text")
        await gpt_3_correct(ctx, text)


def setup(bot):
    bot.add_cog(OpenAI(bot))
