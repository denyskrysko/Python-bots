import time
import requests
from lxml import html
from bs4 import BeautifulSoup
import schedule
import datetime
import urllib.request


def parse(url):
    try:
        page = requests.get(url)
        tree = html.fromstring(page.content)
        name = tree.xpath('//div[@class="quote-ticker tickerLarge"]/text()')
        value = tree.xpath('//div[@class="quote-price priceLarge"]/span/text()')
        Arr = {
            'name': name,
            'value': value
        }

        # response = requests.get(url, timeout=5)
        # content = BeautifulSoup(response.content, "html.parser")
        # Arr = []
        # for element in content.findAll('div', attrs={"class": "quote-details"}):
        #     Arr = {
        #         'name': element.find('div', attrs={"class": "quote-ticker tickerLarge"}).text.encode('utf-8'),
        #         'price': element.find('div', attrs={"class": "quote-price priceLarge"}).text.encode('utf-8'),
        #     }

        return Arr
    except Exception as e:
        print(e)


def telegram_bot_sendtext(bot_message):
    bot_token = '712175175:AAHXStBiBHKgCvtfv87hRfID2yc207j-dd4'
    bot_chatID = '-337657336'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' \
                + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def report(symbol, target):
    # current_dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        Arr = parse('https://web.tmxmoney.com/quote.php?qm_symbol=' + symbol + '&locale=EN')
        message = "Heads up! " + str(Arr['name']).strip("['']") + " Stock level reached: " + \
                  ": $" + str(Arr['value']).strip("['']")
        value = str(Arr['value']).strip("['']")

        if float(value) >= float(target):
            global counter
            if counter == 0:
                telegram_bot_sendtext(message)
                print(" --- M3lvin stock tracking---> " + message)
            counter = + 1
    except Exception as e:
        print(e)


# Entry point - user input
stock_symbol = input("To get a quote enter the stock symbol: ")
stock_target = input("What is the Stock target? ")

counter = 0  # creating global variable for the report function

# schedule.every().day.at("16:50").do(report())
# schedule.every().day.at("13:30").do(report())

while True:
    schedule.run_pending()
    report(stock_symbol, stock_target)
    time.sleep(5)
