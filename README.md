![CROWNBOT-ex-01](https://user-images.githubusercontent.com/45272685/124843493-45b78e80-df4f-11eb-80a0-0e87ec07f260.png)

# Information

CROWNBOT is a discord bot that harnesses bleeding edge AI models to simplify your modertation experience and help retain members with fun features. 


### Stay updated on your favorite idols
We support subscribing to Weverse pages and sending all new posts/comments into a channel. 
This feature is provided by Mujykun's Weverse API library. 

### AI Driven moderation
We use advanced AI to assist in moderating your server. 
Images are run through deep learning networks that can automatically detect innapropriate content. 
We use advanced NLP models to classify text and find potentially problematic statements or people that might need to be supported. 

* Planet Express Labs assumes no responsiblity in the event of false negative/positive events. 
* These features are to assist existing moderation, and should not be considered a complete replacement.




# Install

Hosted CROWNBOT is not running on the Azure Ubuntu:latest image. We have a ~~test~~ temporary production environment running on Heroku and our
deveopers mostly use Windows. There should not be issues with running on different platforms, however we recomend you
follow our environment as close as possible.

### Docker images will be released at some point in the future. 

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
