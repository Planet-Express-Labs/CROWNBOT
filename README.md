![CROWNBOT-ex-01](https://user-images.githubusercontent.com/45272685/124843493-45b78e80-df4f-11eb-80a0-0e87ec07f260.png)


# Install

Hosted CROWNBOT is running on the Azure Ubuntu:latest image. We have a test environment running on Heroku and our
deveopers mostly use Windows. There should not be issues with running on different platforms, however we recomend you
follow our environment as close as possible.

Installation is simple.

1. Run `git clone https://github.com/Planet-Express-Labs/CROWNBOT.git`in a terminal in whatever directory you want the
   server to be stored in.
2. Edit the config_template file and save as `config.ini`. More detailed instructions are inside the file.

   a: Make a bot account here: discord.com/developers/

   b: Make an account on huggingface.co/

   b: To copy the chanel ids, you need to enable developer mode in the settings.

   c: Under the right click menu, there should be an option to copy ids. You need to do this in order to configure the
   bot correctly. To get the server's id, right click the guild name in the upper left.

   d: Configure logging.

   e: ***Save the file as `config.ini`!***

3. Run the bot by opening the bot's directory in the termainal and run `python bot.py`. Depending on your installation,
   you might need to use the specific python version instead (ie. python3.7 or python3).
4. Set up is done. This process will likely change soon as we impliment features. View below for more details on what
   will change and how this will effect you.

# Planned features.

- [ ] Docker image.
    - We'd likely publish a docker image which would be what we'd be primarily supporting, since it's more consistant.
      Of course, this doesn't mean we're going to not support anything outside of docker.
- [x] Local logging should transition to Redis or SQL sometime soon. When this transition finishes, you'll be expected
  to be using one of those two implimentation - text based logging will no longer be supported, and as such must be
  expected to break. We will add this as in opt-in feature initially, then make it the default in future versions.
    - I will likely add support for Redis and SQL through an enternal database or an internal `sqlite3` database for
      simplifying use. Performance will be reduced with this database.
- [x] Multiple server support. This should be relatively simple to add, but I haven't had the time to do anything
  greater then fixing issues when something breaks. This should be added in the coming months, once I have time.
    - Per server logging into a channel (All confessions from within that server will be dumped into this channel.
    - Logging indicator if the host or server has enabled
    - For now, the server's data will be store solely with an internal sqlite3 database. This will probably change much
      later on - after merging to stable.
    - We will still maintain a version without multi server support since it's easier to install and requires less
      resources, but that branch will not recieve frequent updates, and will probably not get feature updates.
- "Private" votes in confession channels.
- [x] ~~New name, new logo/icon. ~~

