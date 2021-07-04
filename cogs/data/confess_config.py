# This software is provided free of charge without a warranty.
# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was 
# this file, You can obtain one at https://mozilla.org/MPL/2.0/.


import codecs
import configparser
import logging
import os

use_env_var = False
log = logging.getLogger(__name__)
try:
    CONFIG_FILE = os.getcwd() + "\\cogs\\data\\config.ini"
except FileNotFoundError:
    use_env_var = True
config = configparser.ConfigParser()
config.read_file(codecs.open(CONFIG_FILE, "r+", "utf-8"))


def read_config(section, value, file="./data/config.ini"):
    config.read_file(codecs.open(file, "r+", "utf-8"))


MAX_BACKUPS = config.get("db", "max_backups")

####################
#       bans       #
####################

#
# def get_bans():
#     with open("./data/bans.csv", newline='') as file:
#         names = []
#         read = csv.reader(file, delimiter='\n', quotechar='|')
#         for row in read:
#             names.append(row)
#         return names
#
#
# def get_user_ban(name):
#     if not os.path.isfile("./data/bans.csv"):
#         file = open("./data/bans.csv", "w")
#         file.close()
#     bans = get_bans()
#     for each in bans:
#         if each == name:
#             return True
#     return False
#
#
# I highly doubt this is remotely close to the correct way of doing something like this, but it is what it is, I guess.
# def rm_ban(user):
#     with open("./data/bans.csv", newline='') as read_file:
#         read = csv.reader(read_file, delimiter='\n', quotechar='|')
#         file = []
#         for each in read:
#             if each != user:
#                 file.append(each)
#     with open("./data/bans.csv", 'w+', newline='') as write_file:
#         write = csv.writer(write_file, delimiter='\n', quotechar='|')
#         for each in file:
#             write.writerow(each)
#
#
# def add_ban(user):
#     if get_user_ban(user):
#         return False
#     with open("./data/bans.csv", "a", newline='') as write_file:
#         write = csv.writer(write_file, delimiter='\n', quotechar='|')
#         user = [user]
#         write.writerow(user)
