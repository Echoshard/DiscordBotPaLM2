#---------TOKEN AND KEYS----------------

#Discord bot Key
DISCORD_BOT_TOKEN = "DISCORD_TOKEN"

#Palm2 API Key
PALM2_API_KEY = "PALM_API_TOKEN"


#Model Settings for Generate Text
DEFAULT_GENERATE_TEXT = {
  'model': 'models/text-bison-001',
  'temperature': 0.6,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 200,
  'stop_sequences': []
}

#---------BOT MEMORY----------------

#How many messages are stored - 6 messages is 3 responses and 3 user messages
MESSAGE_MAX_HISTORY = 8
HAS_MEMORY = True


#Bot Description for Discord
BOTDESCRIPTION = "I am an AI powered bot ready to help!"

#---------CHAT SETTINGS----------------

#This will switch the bot from using generate text to chat API. Allowing you to give it a context and example responses
#Generate text is much faster
USE_CHAT = False

#Model Settings for Chat
DEFAULT_CHAT = {
  'model': 'models/chat-bison-001',
  'temperature': 0.25,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
}


#Bot Context
BOT_CONTEXT = ""
#Shakespeare Bot Example
#BOT_CONTEXT = "Roleplay as AI that speaks like Shakespeare \n"



