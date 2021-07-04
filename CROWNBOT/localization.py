# This software is provided free of charge without a warranty.
# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was 
# this file, You can obtain one at https://mozilla.org/MPL/2.0/.
import logging
from json import loads
from typing import Optional

# from CROWNBOT.config import BOT_LANGUAGE

log = logging.getLogger(__name__)

# TODO: implement per-server
with open(f"./data/en_us.json", "r") as read_strings:
    STRINGS = loads(read_strings.read())

# Maybe we shouldn't be handling version through localization... whatever
REQUIRED_STRING_LIST = [
    "BOT_ABOUT",
    "CMD_PERMISSION_ERROR",
    "COMMAND_ON_COOLDOWN",
    "VERSION",

    "COMMAND_EMPTY_USER_ID",
    "NO_RESULTS",
    "MESSAGE_SENT",
    "COMMAND_EMPTY",
    "BANNED_COMMAND",
    "DISABLED_COMMAND",
    "UNKNOWN_ERROR",
    "INTEGER_ERROR",

    "SETUP_1",
    "SETUP_1_ROLE",
    "SETUP_1_SUCCESS",
    "SETUP_2",
    "SETUP_2_SUCCESS",
    "SETUP_ISSUE_1",
    "SETUP_ISSUE_2",
    "SETUP_ISSUE_3"
]

# Check for all strings.
for s in REQUIRED_STRING_LIST:
    if STRINGS.get(s) is None:
        raise Exception(f"String {s} missing or localization file is missing. The bot cannot start up. ")


def get_string(string_name: str) -> Optional[str]:
    return STRINGS.get(string_name)
