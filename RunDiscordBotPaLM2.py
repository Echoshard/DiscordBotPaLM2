#DiscordPlam2ChatBot

import discord
from discord.ext import commands


#imports from BotConfig
from botConfig import DISCORD_BOT_TOKEN
from botConfig import BOTDESCRIPTION
from botConfig import MESSAGE_MAX_HISTORY
from botConfig import PALM2_API_KEY
from botConfig import BOT_CONTEXT
from botConfig import HAS_MEMORY
from botConfig import USE_CHAT
from botConfig import DEFAULT_GENERATE_TEXT
from botConfig import DEFAULT_CHAT

#Memory System  
message_history_chat = {}

#Discord Intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

#PaLM 2
import google.generativeai as palm
palm.configure(api_key=PALM2_API_KEY)

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
    command_msg = await ExtraCommands(message_str,message.author.name)
    if (command_msg != None):
        await message.add_reaction('🤖')
        await message.channel.send(command_msg)
        return
    #Bot Gets Mentioned
    if bot.user.mentioned_in(message):
         async with message.channel.typing():
            print("New Mention from {message.author.name}! :" + message_str)
            output = WaitForAPI(message_str,message.author.name)
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
            output = WaitForAPI(message_str,message.author.name)
            if output != None:
                #split if message is too long
                await send_messages(message,split_string(output,1700))
                await message.add_reaction('✅')
            else:
                await message.author.send("Failed To Answer")
                await message.add_reaction('❌')

def WaitForAPI(message, userID):
    if USE_CHAT:
        return WaitForAPIChat(message,userID)
    else:
        return WaitForAPIGenerate(message,userID)


#Example using Chat mode Trainable
def WaitForAPIChat(message,user_id):
    global message_history_chat
    global history_count
    
    #Holder for Errors
    extra_text = ""

    #check for Key
    if user_id not in message_history_chat:
        message_history_chat[user_id] = []
        print("New Chat Found adding " + str(user_id))
    #add the message
    message_history_chat[user_id].append(message)

    #Talk to API
    response = palm.chat(
    **DEFAULT_CHAT,
    context=BOT_CONTEXT,
    messages=message_history_chat[user_id]
    )
    #Check For Errors
    if not response.last:
            print(message + "Failed to Send")
            return None
    
    #If more messages then chat history remove the top one 
    if len(message_history_chat[user_id]) >= MESSAGE_MAX_HISTORY:
        message_history_chat[user_id].pop(0)

    #if memory disabled ignore
    if HAS_MEMORY == False:
        del message_history_chat[user_id]
    #print(message_history_chat[user_id])
    message_history_chat[user_id].append(response.last)
    return response.last + extra_text

#Example just using text completion mode
def WaitForAPIGenerate(message,user_id):
    global message_history_chat
    global history_count
    extra_text = ""

    #
    if user_id not in message_history_chat:
        message_history_chat[user_id] = []
        print("New Chat Found adding " + str(user_id))
    message_history_chat[user_id].append(message)

    #Talk to API generate
    response = palm.generate_text(
    **DEFAULT_GENERATE_TEXT,
    prompt=' '.join(message_history_chat[user_id])
    )

    #if Result errors 
    if not response.result:
            print(message + "Failed to Send")
            return None

    #If more messages then chat history remove the top one 
    if len(message_history_chat[user_id]) >= MESSAGE_MAX_HISTORY:
        message_history_chat[user_id].pop(0)

    #if memory disabled ignore
    if HAS_MEMORY == False:
        del message_history_chat[user_id]
    #A Debug tester
    #print(message_history_chat[user_id])
    message_history_chat[user_id].append(response.result)
    return response.result + extra_text

#string splitter if it gets too long
def split_string(string, max_length):
    messages = []
    for i in range(0, len(string), max_length):
        sub_message = string[i:i+max_length]
        messages.append(sub_message)
    return messages

async def send_messages(messageSystem,output):
    for index, string in enumerate(output):
        await messageSystem.channel.send(string)

async def ExtraCommands(message,user_id):
    global message_history_chat
    if message.startswith("COM"):
        command_message = message.replace("COM ",'')
        match command_message:
            case "Reset":
                if user_id in message_history_chat:
                    del message_history_chat[user_id]
                return "***Deleteing History Reset to Default***"
            #Add extra  cases for later!
            #case 2: 
            #    print("Two")
            #case 3:
            #    print("Three")
        command_message = "Command was not correct you can use ***COM Reset*** to clear my memory"
        return command_message
    return

#Run the Bot!
bot.run(DISCORD_BOT_TOKEN)
