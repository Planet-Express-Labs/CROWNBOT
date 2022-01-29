# This software is provided free of charge without a warranty.
# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was
# this file, You can obtain one at https://mozilla.org/MPL/2.0/.

from sqlalchemy import Column, BigInteger, Boolean, String
from sqlalchemy.ext.hybrid import hybrid_property
from sessions import *


class WeverseChannel(Base):
    __tablename__ = 'confess_data'

    channel_id = Column(BigInteger, null=True, blank=True, primary_key=True)
    role_id = Column(BigInteger, null=True, blank=True)
    media_enabled = Column(Boolean, null=True, blank=True)
    comments_enabled = Column(Boolean, null=True, blank=True)
    _already_posted = Column(String, null=True, blank=True)

    @hybrid_property
    def already_posted(self):
        return self._already_posted.split(',')

    @already_posted.setter
    def already_posted(self, posts):
        self._already_posted = ','.join(posts)
