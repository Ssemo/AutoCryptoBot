import ccxt
import time
from dotenv import load_dotenv
import os

load_dotenv()  # قراءة .env

exchange = ccxt.binance({
    'apiKey': os.getenv('BINANCE_API_KEY'),
    'secret': os.getenv('BINANCE_SECRET'),
    'enableRateLimit': True,
    'options': {'defaultType': 'spot'}
})

symbol = 'SOL/USDT'
buy_threshold = 140  # اشتري إذا تحت ده
sell_threshold = 150  # بيع إذا فوق ده
amount = 0.1  # كمية صغيرة للتجربة

while True:
    ticker = exchange.fetch_ticker(symbol)
    price = ticker print(f'سعر SOL/USDT الحالي: {price} USDT')

    balance = exchange.fetch_balance()
    usdt = balance  sol = balance  if price < buy_threshold and usdt > amount * price:
        print("شراء...")
        exchange.create_market_buy_order(symbol, amount)
    elif price > sell_threshold and sol > amount:
        print("بيع...")
        exchange.create_market_sell_order(symbol, amount)

    time.sleep(60)  # انتظر دقيقة قبل الفحص الجديد
