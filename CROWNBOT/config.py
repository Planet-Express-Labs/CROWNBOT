# This software is provided free of charge without a warranty.
# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was 
# this file, You can obtain one at https://mozilla.org/MPL/2.0/.

import codecs
import configparser
import logging
import os
import openai

log = logging.getLogger(__name__)
use_env = False
required_vars = ["token", "logging", "developer", "admin"]


class MissingEnvironmentVariableError(Exception):
    """Raised when a value is not found in the environment variables. """
    pass


if not os.path.exists(os.getcwd() + "\\data\\config.ini"):
    print("Config file missing! Attempting to use environment variables. ")
    for each in required_vars:
        # checks each required variable if it exists and raises an exception if it isn't.
        temp = os.getenv("zoidberg_" + each)
        if temp is None:
            print(each)
            raise MissingEnvironmentVariableError

    BOT_TOKEN = os.getenv("zoidberg_token")
    LOGGING_LEVEL = os.getenv("zoidberg_logging")
    DATABASE = os.getenv("zoidberg_database_path")
    # These will be removed later.
    DEV_ID = os.getenv("zoidberg_developer").split(",")
    ADMIN_ID = os.getenv("zoidberg_admin").split(",")
    TEST_GUILDS = os.getenv("zoidberg_guilds")
    if TEST_GUILDS is not None:
        TEST_GUILDS = TEST_GUILDS.split(",")
    HF_API_KEY = os.getenv("zoidberg_huggingface")
    SUBSCRIPTION_KEY = os.getenv('zoidberg_content_moderator_api_key')
    CONTENT_MODERATOR_ENDPOINT = os.getenv("zoidberg_content_moderator_endpoint")
    AI21_API_KEY = os.getenv("zoidberg_ai21")
    GREYNOISE_API_KEY = os.getenv("zoidberg_greynoise")

    WEVERSE_API_KEY = os.getenv("zoidberg_weverse")
    WEVERSE_USERNAME = os.getenv("zoidberg_weverse_username")
    WEVERSE_PASSWORD = os.getenv("zoidberg_weverse_password")
    WEVERSE_IMAGE_STORE = os.getenv("zoidberg_weverse_image_store")

else:
    CONFIG_FILE = os.getcwd() + "\\data\\config.ini"
    config = configparser.ConfigParser()
    config.read_file(codecs.open(CONFIG_FILE, "r+", "utf-8"))


    def read_config(file=CONFIG_FILE):
        config.read_file(codecs.open(file, "r+", "utf-8"))


    # Bot section.
    TEST_GUILDS = config.get("Bot", "testing_guilds").split(" ")

    DATABASE = config.get("Bot", "database_path")
    BOT_TOKEN = config.get("Bot", "bot_token")

    LOGGING_LEVEL = config.get("Bot", "logging_level")
    DEV_ID = config.get("Users", "developer_id")

    ADMIN_ID = config.get("Users", "admin_ids").split(" ")

    # AI section:
    HF_API_KEY = config.get("AI", "HuggingFace_api_key")
    SUBSCRIPTION_KEY = config.get("AI", "content_moderator_api_key")
    CONTENT_MODERATOR_ENDPOINT = config.get("AI", "content_moderator_endpoint")
    AI21_API_KEY = config.get("AI", "ai21_api_key")
    openai.api_key = config.get("AI", "openai_api_key")

    # API section
    GOOGLE_API_KEY = config.get("API", "google_api_key")
    GREYNOISE_API_KEY = config.get("API", "greynoise_api_key")
    WEVERSE_API_KEY = config.get("API", "weverse_api_key")
    WEVERSE_USERNAME = config.get("API", "weverse_username")
    WEVERSE_PASSWORD = config.get("API", "weverse_password")
    WEVERSE_IMAGE_STORE = config.get("API", "weverse_image_store")

