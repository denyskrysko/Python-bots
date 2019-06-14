import discord
from discord.ext import commands
import aiml
import os

from pip._vendor.distlib.compat import raw_input

client = commands.Bot(command_prefix="%")
TOKEN = "NTg4NDY5NDk0MjU5NjQ2NjQy.XQO92Q.e-tlPFsabdgC17uxQZd8auXWLjc"
kernel = aiml.Kernel()
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")


# if os.path.isfile("bot_brain.brn"):
#     kernel.bootstrap(brainFile = "bot_brain.brn")
# else:
#     kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
#     kernel.saveBrain("bot_brain.brn")
#
# while True:
#     message = raw_input("Enter your message to the bot: ")
#     if message == "quit":
#         exit()
#     elif message == "save":
#         kernel.saveBrain("bot_brain.brn")
#     else:
#         bot_response = kernel.respond(message)
        # Do something with bot_response

# Greeting
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await client.process_commands(message)

    # AI starts here
    channel = message.channel
    try:
        await channel.send(kernel.respond(message.content))
    except:
        print("Hit an error")


client.run(TOKEN)
