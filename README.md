# Discord Bot PaLM2
A simple Discord bot example that uses PaLM2 Api.

# Setup 
## Step 1: Edit 

Open ```botConfig.py``` and replace the default text with your Discord Bot Token and your PaLM2 API Key 

> Getting your Discord Bot Token -https://discordpy.readthedocs.io/en/stable/discord.html

```DISCORD_BOT_TOKEN = "DISCORD TOKEN""```

> Getting your PaLM2 Key - https://makersuite.google.com/waitlist

```PALM2_API_KEY = "PALM API KEY"```

  ### Step 2: Install Requirements
    pip install -r requirements.txt
  ### Step 3: Run 
    python RunDiscordBotPaLM2.py
  ## Bot Usage

  The bot will respond a persons DM's and mention in any channel it has access to. 

  ## Memory:

  This Bot has a simple memory system it is off by default and can be enabled by ```HAS_MEMORY``` = True It keeps track of the ```MESSAGE_MAX_HISTORY``` and can be reset by typing ```COM Reset``` It is best to disable this if you are going to use it with many people as the memory

  # Chat and Prompt
  The bot is defaulted to text generation. this gives much faster generation. changing the bot to chat mode will allow you to give it a personality and alter it. You can enable the chat mode by changing ```USE_CHAT``` to true. <p>

  ## Context and Example Messages

  The bots personlity can be adjusted here forcing all text to go through this filter like a lense. change  ```BOT_CONTEXT```

  ### Examples
  
    Roleplay as AI that speaks like Shakespeare
  
  Everything is answered in fancy english <p>
    
    Given a topic, you will use emoji's while answering
  Adds Emoji's to everything it says <p>

  More examples can be found at https://developers.generativeai.google/prompt-gallery?type=chat <p>
  ### Example Messages
  Example messages allow you to even further fine tune responses these examples are at
  https://makersuite.google.com/app/prompts/new_multiturn
   
