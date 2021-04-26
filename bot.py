import time
import schedule
import requests


def telegram_bot_sendtext(bot_message):
    
    bot_token = '1362189622:AAEB8Z7NxGsjNRHvGmXCcGB1iUod4Tmo0aQ'
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def report():
    my_balance = 10   ## Replace this number with an API call to fetch your account balance
    my_message = "Current balance is: {}".format(my_balance)   ## Customize your message
    telegram_bot_sendtext(my_message)


    
schedule.every().day.at("12:00").do(report)

while True:
    schedule.run_pending()
    time.sleep(1)