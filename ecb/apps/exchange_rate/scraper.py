import requests

from bs4 import BeautifulSoup
from dateutil import parser
from decimal import Decimal

from .models import Currency, ExchangeRate


class ExchangeRateScraper:
    SCRAPER_URL = 'https://www.ecb.europa.eu/rss/fxref-%s.html'

    def __init__(self, symbol):
        self.symbol = symbol

    def get_exchange_rate_rss(self):
        response = requests.get(self.SCRAPER_URL % self.symbol.lower())

        if response.status_code == 200:
            return response.content

    def get_currency_object(self):
        try:
            return Currency.objects.get(symbol=self.symbol)
        except Currency.DoesNotExist:
            pass

    def get_latest_exchange_rate(self):
        exchange_rate_rss = self.get_exchange_rate_rss()
        if exchange_rate_rss is not None:
            scraper = BeautifulSoup(exchange_rate_rss, 'xml')
            item = scraper.find('item')
            statistics = item.find('statistics')

            exchange_rate = {
                'currency': self.get_currency_object(),
                'rate': Decimal(statistics.find('value').text),
                'date': parser.parse(item.find('date').text)
            }

            return exchange_rate

    def save_latest_exchange_rate(self):
        latest_exchange_rate = self.get_latest_exchange_rate()
        if latest_exchange_rate is not None and isinstance(latest_exchange_rate, dict):
            exchange_rate = ExchangeRate(**latest_exchange_rate)
            exchange_rate.save()
