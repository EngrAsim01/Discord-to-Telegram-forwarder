import discord
import requests
import keep_alive

# Discord Bot Token
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Telegram Bot Token
TELEGRAM_BOT_TOKEN = "Your Telegram bot token"

# Telegram Chat ID
TELEGRAM_CHAT_ID = "Telegram group id or channel id to which you want the msg to be sent. "

# setting the on msg event like when a msg is recieved in discord group this will be executed.
@client.event
async def on_message(message):
  
  # if the msg is sent by the bot itself it will return.
  # means the bot will not process that msg.
    if message.author == client.user:
        return

    # Check if the message has an attachment (i.e. a file)
    if message.attachments:
        try:
            # Get the first attachment (assuming there's only one)
            attachment = message.attachments[0]

            # Download the file
            file = requests.get(attachment.url)
        
            # if you want to save the file in your memory you can uncomment this code...
            # # Save the file to disk
            # with open("file.doc", "wb") as f:
            #   f.write(file.content)
        
            # Forward the file to Telegram
            requests.post(
                f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendDocument",
                data={
                "chat_id": TELEGRAM_CHAT_ID,
                #   "reply_to_message_id": text
                },
                files={"document": ("file.doc", file.content)})
            
            #   print(f"Telegram API request result: {response.text}")

        except Exception as e:
            print(e)
            print('error')
    
    elif message.content:

        try:
    
            # This is the text of the msg 
            text = message.content
             
            # Forward the text to Telegram
            requests.post(
                f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
                data={
                "chat_id": TELEGRAM_CHAT_ID,
                "text" : text
                })
                 
            #   print(f"Telegram API request result: {response.text}")

        except Exception as e:
            print(e)
            print('error')


# this is a flask app code which you will need if you want your code to run 24/7 on replit
keep_alive.keep_alive()

# Start the Discord bot
client.run("Your discord bot api token")
