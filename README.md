# ربات سیگنال‌دهنده ارز دیجیتال

این پروژه یک ربات تلگرام هوشمند برای تحلیل و سیگنال‌دهی جفت‌ارزهای دلاری (USDT) در صرافی CoinEx است.

## ویژگی‌ها:
- تحلیل داده‌های CoinEx و Binance
- بررسی همه‌ی تایم‌فریم‌ها (15 دقیقه، 1 ساعته، 4 ساعته، روزانه)
- استفاده از اندیکاتورهای:
  - RSI
  - MACD
  - EMA
  - Bollinger Bands
  - CCI
  - Ichimoku
  - Volume
  - Momentum
- دریافت اخبار و توییت‌های مهم (غیرفارسی)
- بررسی لیست شدن ارزها، ترندها و...
import requests

TOKEN = "7787584418:AAFnL7cLdaw4NgyKdmJOqMvd7GRGL8zgks8"
CHAT_ID = "6393521721"
TEXT = "سلام! این یه تسته که مطمئن بشیم ارسال پیام درسته."

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = {
    "chat_id": CHAT_ID,
    "text": TEXT
}

response = requests.post(url, data=data)import requests

TOKEN = "7787584418:AAFnL7cLdaw4NgyKdmJOqMvd7GRGL8zgks8"
CHAT_ID = "6393521721"
TEXT = "تست که مطمئن بشیم پیام درسته"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = {
    "chat_id": CHAT_ID,
    "text": TEXT
}

response = requests.post(url, data=data)
print(response.text)
print(response.text)
## خروجی ربات:
- نقطه ورود
- استاپ‌لاس (۱٪ پایین‌تر از ورود)
- سه تارگت (TP1 = ۲٪، TP2 = ۴٪، TP3 = ۵٪)
- لوریج مناسب

> طراحی شده برای تحلیل ۲۰ جفت‌ارز برتر دلاری CoinEx و گسترش در آینده

---

**توسعه‌دهنده:** رضا  
**نام کاربری تلگرام:** @Fzrtsh
