from discord.ext import commands
import aiml
from datetime import datetime
from datetime import timedelta


client = commands.Bot(command_prefix="%")
TOKEN = "NTg4NDY5NDk0MjU5NjQ2NjQy.XQO92Q.e-tlPFsabdgC17uxQZd8auXWLjc"
kernel = aiml.Kernel()
kernel.learn("brain.aiml")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    channel = message.channel
    await client.process_commands(message)
    now = datetime.now().strftime('%d-%m-%y %H:%M')
    user_input = datetime.strptime(message.content, '%d-%m-%y %H:%M')
    first_notific = user_input - timedelta(minutes=5)
    second_notific = user_input - timedelta(minutes=15)
    print(now)
    print(user_input)
    print(first_notific)
    # print(datetime.strptime(second_notific, '%d-%m-%y %H:%M'))
    try:
        if now == first_notific:
            await channel.send("test 5 min - " + str(first_notific))
            # await channel.send(kernel.respond(message.content))
        if now == second_notific:
            await channel.send("test 15 min - " + str(second_notific))
    except:
        print("Hit an error")


client.run(TOKEN)




