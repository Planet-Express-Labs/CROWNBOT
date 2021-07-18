# This software is provided free of charge without a warranty.
# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was 
# this file, You can obtain one at https://mozilla.org/MPL/2.0/.

import os

from discord.ext import commands, tasks

schedule = []  # each item should look like [time, repeatevery, description]


def readschedule():
    with open(os.getcwd() + "\\data\\schedules.cfg", "r") as file:
        semi = file.read().split('-')
        for i in semi[:int(len(semi)) - 1]:
            supersemi = i.split('|')
            schedule.append(supersemi[:int(len(supersemi)) - 1])

        print(schedule)


def storeschedule():
    with open(os.getcwd() + "\\data\\schedules.cfg", "w") as file:
        finalstr = ""
        for i in schedule:
            for x in i:  # baddd
                finalstr += x + "|"
            finalstr += "-"

        file.write(finalstr)


class Schedule(commands.Cog):
    @tasks.loop(seconds=30)
    async def repeater(self):
        pass

    @commands.command(name="update_schedule")
    async def cmd_update_schedule(self, ctx):
        readschedule()

    @commands.command("add_schedule")
    async def cmd_add_schedule(self, ctx, time, repeats, item):
        schedule.append([time, repeats, item, ctx.author.id])
        await ctx.send("You have scheduled item " + item + " at " + time + " which will repeat " + repeats + " times.")
        storeschedule()


def setup(bot):
    bot.add_cog(Schedule(bot))
