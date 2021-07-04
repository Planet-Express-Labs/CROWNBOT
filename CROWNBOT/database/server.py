# This software is provided free of charge without a warranty.
# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was 
# this file, You can obtain one at https://mozilla.org/MPL/2.0/.
from sqlalchemy import Column, String, Integer

from CROWNBOT.database import database
from sessions import Base


class Server(Base):
    __tablename__ = 'server_data'

    guild = Column(Integer, primary_key=True)
    enabled_modules = Column(String)  # Reserved for future use
    # I'll probably change this to something that will allow more then just two levels of permission, but that's later.
    # If admin_role == 0, then it's just going to go off of each role's permissions.
    admin_role = Column(bool)
    mod_role = Column(bool)
    cooldown = Column(Integer)  # Reserved for future use
    auto_delete = Column(Integer)  # Reserved for future use
    premium = Column(bool)  # Reserved for future use
    official_guild = Column(bool)

    def __init__(self, enabled_modules, guild, admin_role, mod_role, cooldown, auto_delete, premium, official_guild):
        self.guild = guild
        self.enabled_modules = enabled_modules
        self.admin_role = admin_role
        self.mod_role = mod_role
        self.cooldown = cooldown
        self.auto_delete = auto_delete
        self.premium = premium
        self.official_guild = official_guild


def get_server():
    session = database.make_sessions()
    server = session.query(Server)
    session.close()
    return server.all()


def initialize_server(guild, enabled_modules, admin_role, mod_role, auto_delete, premium):
    session = database.make_sessions()
    server = Server(guild, enabled_modules, admin_role, mod_role, None, auto_delete, premium, False)
    database.close_session(session, server)
