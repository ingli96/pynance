import asyncio
from utils import get_date
from binance.client import Client


def main():

    data = client.get_klines(symbol='BNBUSDT', interval='1M', startTime='1628360070000')
    for i in data:
        print('date:', get_date(i[0]), '~ value:', i[4])


if __name__ == "__main__":
    client = Client("", "")
    main()
