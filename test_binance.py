import ccxt
from dotenv import load_dotenv
import os

load_dotenv()

exchange = ccxt.binance({
    'apiKey': os.getenv('BINANCE_API_KEY'),
    'secret': os.getenv('BINANCE_API_SECRET'),
    'enableRateLimit': True,
    'options': {'defaultType': 'spot'}
})

try:
    balance = exchange.fetch_balance()
    print("الرصيد الحالي:")
    print(balance)
except Exception as e:
    print("في خطأ:", str(e))
