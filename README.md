# DiscordBotPaLM2

A simple Discord bot example that uses PaLM2 Api.


## Step 1: Edit ```botConfig.py```

Add your Discord Key and your PaLM2 API Key 

> Getting your Discord Key -https://discordpy.readthedocs.io/en/stable/discord.html

```DISCORD_API_KEY = "DISCORD KEY"```

> Getting your PaLM2 Key - https://makersuite.google.com/waitlist

```PALM2_API_KEY = "PALM API KEY"```

## Step 2: Install Requirements
```pip install -r requirements.txt```

## Step 3: Run 
```python RunDiscordBotPaLM2.py```

## Bot Usage

It will respond a persons DM's and you mention in any channel it has access to. 

## Memory:

This Bot has a simple memory system it is off by default and can be enabled by ```HAS_MEMORY``` = True It keeps track of the ```MESSAGE_MAX_HISTORY``` and can be reset by typing ```COM Reset``` It is best to disable this if you are going to use it with many people as the memory
