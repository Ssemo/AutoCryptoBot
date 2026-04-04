import ccxt
import time
from dotenv import load_dotenv
import os

load_dotenv()

exchange = ccxt.binance({
    'apiKey': os.getenv('BINANCE_API_KEY'),
    'secret': os.getenv('BINANCE_SECRET'),
    'enableRateLimit': True,
    'options': {'defaultType': 'spot'},
})

exchange.enable_demo_trading(True)  # يفعل الديمو

print("جاري جلب سعر SOL/USDT...")

try:
    ticker = exchange.fetch_ticker('SOL/USDT')
    price = float(ticker )
    print(f"سعر SOL/USDT الحالي في الديمو: ${price:.2f}")
except Exception as e:
    print(f"خطأ: {str(e)}")