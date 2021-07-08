# In depth setup guide

This bot is not particularly easy to self-host. We recommend using our hosted solutions. 
We do not put too much effort into making this bot easy to host locally, 
and as such will not be able to offer much support for self-hosting. 
For more information of our hosted bots, go to [our website](https://bots.pexl.pw).

At the moment, builds on docker are not being made. We plan to change this at a later date as we look
into using a solution like Kubernetes. 
For more information, view [this github issue](https://github.com/Planet-Express-Labs/ZoidbergBot/issues/21). 
This issue serves an area to track progress on support for Docker. This probably doesn't link to the correct bot, 
but this isn't an issue because rollout of docker images is planned to be released across everything at the same time.

You'll need API keys for Discord, Huggingface, and OpenAI. If you are unable to figure out how to gather those keys,
you probably should just use the hosted variant. You'll also need some way to use a database. We support PostgreSQL and
SQLite. THe SQLite database is the default, however cannot be used with services that do not have persistent storage. 
You'll also need at least one Lavalink node. Some time down the road, we will be requiring a server that can host
Tensorflow. This will require storage space of around 128gb, we recommend this to be persistent as the models will need
to be downloaded in full at every reboot of this node. 


