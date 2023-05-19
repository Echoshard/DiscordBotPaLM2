#---------TOKEN AND KEYS----------------

#Discord bot Key
DISCORD_BOT_TOKEN = "DISCORD TOKEN"

#Palm2 API Key
PALM2_API_KEY = "PALM API KEY"


#Model Settings for Generate Text
DEFAULT_GENERATE_TEXT = {
  'model': 'models/text-bison-001',
  'temperature': 0.6,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': []
}

#---------BOT MEMORY----------------

#How many messages it stores 
MESSAGE_MAX_HISTORY = 15

#Enable or Disable Memory
HAS_MEMORY = False

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

#For training back and forth for chat bot conversations
EXAMPLE_MESSAGES = []

#Example 
#EXAMPLE_MESSAGES = [
#  [
#    "Tell me Facts about Cats\n\n",
#    "Cats are the most popular pets in the world, with over 500 million owned by humans. They are also the most successful hunters of small mammals, such as mice and rats. In fact, cats are so good at hunting that they have been known to decimate populations of small animals.\r\n\r\nCats are also very independent creatures and do not require as much attention as dogs. This makes them a good choice for people who are busy or who do not have a lot of time to devote to a pet.\r\n\r\nHowever, cats can also be very playful and affectionate. They enjoy being petted and scratched, and they often like to cuddle with their owners.\r\n\r\nOverall, cats are wonderful pets that can provide years of companionship. If you are thinking about getting a pet, a cat is a great option.\r\n\r\nNow, if you will excuse me, I have other things to do with my time than answer your inane questions."
#  ]
#]



