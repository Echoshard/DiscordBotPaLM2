﻿#DiscordPlam2ChatBot

import discord
from discord.ext import commands


#imports from BotConfig
from botConfig import DISCORD_BOT_TOKEN
from botConfig import BOTDESCRIPTION
from botConfig import MESSAGE_MAX_HISTORY
from botConfig import PALM2_API_KEY
from botConfig import HAS_MEMORY

#Memory System  
message_history = ""
history_count = 0   



#Discord Intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True


#PaLM 2
import google.generativeai as palm
palm.configure(api_key=PALM2_API_KEY)

defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.6,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': []
}

#Start the Bot!
bot = commands.Bot(command_prefix='!', description=BOTDESCRIPTION, intents=intents)

#Debug when Ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

#On Message used here to intercept
@bot.event
async def on_message(message):
    #Bot ignores messages to it self
    if message.author == bot.user:
        return
    output = None
    message_str = message.content
    command_msg = await ExtraCommands(message_str)
    if (command_msg != None):
        await message.add_reaction('🤖')
        await message.channel.send(command_msg)
        return
    #Bot Gets Mentioned
    if bot.user.mentioned_in(message):
         async with message.channel.typing():
            print("New Mention from {message.author.name}! :" + message_str)
            output = WaitForAPI(message_str)
            if output != None:
                #split if message is too long
                await send_messages(message,split_string(output,1700))
                await message.add_reaction('✅')
            else:
                await message.author.send("Failed To Answer")
                await message.add_reaction('❌')
    #Bot is DMed!!
    if message.guild is None:
        async with message.channel.typing():
            print(f"New DM from {message.author.name}! :" + message_str)
            output = WaitForAPI(message_str)
            if output != None:
                #split if message is too long
                await send_messages(message,split_string(output,1700))
                await message.add_reaction('✅')
            else:
                await message.author.send("Failed To Answer")
                await message.add_reaction('❌')


def WaitForAPI(message):
    
    global message_history
    global history_count
    extra_text = ""

    #if Memory All this stuff
    if HAS_MEMORY:
        message_history  += " " + message

        #Talk to open AI
        response = palm.generate_text(
        **defaults,
        prompt=message_history
        )
        if not response.result:
                print(message + "Failed to Send")
                return None

        history_count = history_count + 1
        if history_count > MESSAGE_MAX_HISTORY:
            print("----Memory Full Forgetting")
            extra_text = " ***Memory is Full Forgetting***"
            message_history = ""
        message_history = message +  " " + response.result;
    #Skip Memory and just reply
    else:
        response = palm.generate_text(
        **defaults,
        prompt=message
        )
        if not response.result:
            print(message + "Failed to Send")
            return None
    return response.result + extra_text


def split_string(string, max_length):
    messages = []
    for i in range(0, len(string), max_length):
        sub_message = string[i:i+max_length]
        messages.append(sub_message)
    return messages

async def send_messages(messageSystem,output):
    for index, string in enumerate(output):
        await messageSystem.channel.send(string)


#def chatActivationPhrase(message):
#    if message.startswith(IN_CHANNEL_CHAT_PHRASE):
#        return True

async def ExtraCommands(message):
    global message_history
    global history_count
    if message.startswith("COM"):
        command_message = message.replace("COM ",'')
        match command_message:
            case "Reset":
                message_history = "";
                history_count = 0
                return "***Deleteing History Reset to Default***"
            #case 2:
            #    print("Two")
            #case 3:
            #    print("Three")
        command_message = "Command was not correct you can use ***COM Reset*** to clear my memory"
        return command_message
    return

#Run the Bot!
bot.run(DISCORD_BOT_TOKEN)
