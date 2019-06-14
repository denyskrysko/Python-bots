import time
import datetime
import schedule
import requests
import json


def telegram_bot_sendtext(bot_message):
    bot_token = '712175175:AAHXStBiBHKgCvtfv87hRfID2yc207j-dd4'
    bot_chatID = '-337657336'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' \
                + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def report():
    current_dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    my_message = current_dt + " - test msg."
    test = telegram_bot_sendtext(my_message)
    data = test['result']['text']
    print(data)
    # print(test)

report()