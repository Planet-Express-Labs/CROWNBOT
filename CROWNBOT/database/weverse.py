# This software is provided free of charge without a warranty.
# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was
    # this file, You can obtain one at https://mozilla.org/MPL/2.0/.
from sqlalchemy import Column, String, Integer
from server import *
from sessions import *


class Weverse(Base):
    __tablename__ = 'weverse_subscriptions'

    guild = Column(Integer, primary_key=True)
    communities = Column(String).split(',')
    notify_channel = Column(String).split(',')

    def __init__(self, guild, communities, notify_channel):
        self.guild = guild
        self.communities = communities
        self.notify_channel = notify_channel
