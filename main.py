
import time
import requests
import telebot

# تنظیمات ربات
API_KEY = '7787584418:AAFnL7cLdaw4NgyKdmJOqMvd7GRGL8zgks8'
bot = telebot.TeleBot(API_KEY)
USER_ID = 6393521721

def send_signal(message):
    bot.send_message(USER_ID, message)

def get_coinex_data(symbol='BTCUSDT'):
    url = f"https://api.coinex.com/v1/market/kline?market={symbol}&type=15min&limit=10"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None
    except Exception as e:
        return None

def analyze_and_send():
    pairs = ['BTCUSDT', 'ETHUSDT', 'XRPUSDT']
    for pair in pairs:
        data = get_coinex_data(pair)
        if data:
            # تحلیل ساده به عنوان نمونه (میتونه جایگزین بشه با اندیکاتور واقعی)
            prices = [float(c[4]) for c in data['data']]
            if prices[-1] > prices[-2]:
                message = f"سیگنال خرید {pair}: قیمت صعودی است."
                send_signal(message)

# اجرای هر ۱۵ دقیقه یک بار
while True:
    analyze_and_send()
    time.sleep(900)
