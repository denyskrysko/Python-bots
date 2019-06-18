import datetime
import discord
from discord.ext import commands
import aiml
import os


client = commands.Bot(command_prefix="%")
TOKEN = "NTg4NDY5NDk0MjU5NjQ2NjQy.XQO92Q.e-tlPFsabdgC17uxQZd8auXWLjc"
kernel = aiml.Kernel()
# kernel.learn("brain.aiml")

BRAIN_FILE="brain.dump"
if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    kernel.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    kernel.bootstrap(learnFiles="startup.xml", commands="load aiml b")
    print("Saving brain file: " + BRAIN_FILE)
    kernel.saveBrain(BRAIN_FILE)

# Greeting
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await client.process_commands(message)

    # AI starts here
    channel = message.channel
    try:
        if message.content == "load aiml b":
            print("------------------")
            print("Parsing aiml files")
            kernel.bootstrap(learnFiles="startup.xml", commands="load aiml b")
            print("Saving brain file: " + BRAIN_FILE)
            kernel.saveBrain(BRAIN_FILE)
            print("------------------")
        else:
            await channel.send(kernel.respond(message.content))
            print(kernel.respond(message.content))
    except:
        print("Hit an error")


client.run(TOKEN)
