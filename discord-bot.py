import discord
from bs4 import BeautifulSoup
import requests
from discord.ext.commands import Bot
import aiml

BOT_PREFIX = ("?", "!", "$")
TOKEN = "NTg4MDUzMjg1MTM5Nzc1NTY5.XP_mIQ.S9gllAGIgUCv7AZcEB-lofIOX_g"

client = Bot(command_prefix=BOT_PREFIX)
game = "& Watching Pornhub"


# Entry point
@client.event
async def on_ready():
    print('Logged in as ' + client.user.name)
    await client.change_presence(activity=discord.Game(game))


client.remove_command('help')


# Show Help
@client.command()
async def help(context):
    embed = discord.Embed(title="Rockford-bot",
                          description="Я могу показать статистику игроков и всю технику 10-го уровня "
                                      "на которой есть хотя бы 1 бой.",
                          color=0x9900FF)

    await context.send(embed=embed)
    await context.send("Список команд: \n "
                       "\u2022 !stats PLAYER \u2023\u2023\u2023 Отображает общую статистику игрока \n "
                       "\u2022 !tanks PLAYER \u2023\u2023\u2023 Отображает список танков 10-го уровня \n"
                       "\u2022 !news \u2023\u2023\u2023 Отображает новости относящиеся к клану OTB-X(в разработке) \n\n"
                       "Пример: !stast RurikIII \n\n"
                       "Возможные префиксы и aliases для команд: \n"
                       "?, !, $, st, stat, stats, tn, tank, tanks.")


# Show Stats
@client.command(name='stats',
                aliases=['st', 'stat'],
                pass_context=True)
async def stats(context, arg1):
    response = fn_scrape_stats(arg1)
    if "vinney" in arg1:
        await context.send(context.message.author.mention +
                           ', лучше не позориться и не показывать эту стату. Это же {}'.format(arg1))
    else:
        if "HTs:" in response[16][1]:
            await context.send('Привет ' + context.message.author.mention)
            await context.channel.send("Статистика игрока {}:\n".format(arg1) +
                                       response[2][0] + " = " + response[2][1] + "\n" +
                                       response[0][0] + " = " + response[0][1] + "\n" +
                                       response[3][0] + " = " + response[3][1] + "\n" +
                                       response[4][0] + " = " + response[4][1] + "\n" +
                                       response[5][0] + " = " + response[5][1] + "\n")
        else:
            await context.send('Привет ' + context.message.author.mention)
            await context.channel.send("Статистика игрока {}:\n".format(arg1) +
                                       response[2][0] + " = " + response[2][1] + "\n" +
                                       response[0][0] + " = " + response[0][1] + "\n" +
                                       response[3][0] + " = " + response[3][1] + "\n" +
                                       response[4][0] + " = " + response[4][1] + "\n" +
                                       response[5][0] + " = " + response[5][1] + "\n")


# Show Tanks
@client.command(name='tanks',
                aliases=['tn', 'tank'],
                pass_context=True)
async def tanks(context, arg1):
    response = fn_scrape_tanks(arg1)
    response = '\n'.join(response)
    await context.send('Привет ' + context.message.author.mention)
    await context.channel.send("Список танков 10-го уровня игрока {}:\n".format(arg1) + response)


# Scrapping stats data from website
def fn_scrape_stats(nickname):
    url = "https://www.noobmeter.com/player/ru/" + nickname
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')

    data = []
    table = soup.find('table', attrs={'class': 'tablesorter with-rating-colors'})
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])  # Get rid of empty values

    return data


# Scrapping stats data from website
def fn_scrape_tanks(nickname):
    url = "https://www.noobmeter.com/player/ru/" + nickname
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')

    data = []
    table = soup.find('table', attrs={'class': 'tablesorter with-rating-colors'})
    table_body = table.find('tbody')
    spans = table_body.findAll('span')

    for span in spans:
        for span2 in span.findAll('span'):
            data.append(span2.text)

    return data


client.run(TOKEN)
