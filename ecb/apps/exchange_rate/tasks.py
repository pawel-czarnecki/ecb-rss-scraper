from celery import Celery
from celery.utils.log import get_task_logger

from .scraper import ExchangeRateScraper
from .models import Currency

logger = get_task_logger(__name__)
app = Celery('ecb')


@app.task
def task_save_latest_exchange_rate():
    currencies = Currency.objects.all()
    for currency in currencies:
        exchange_rate_scraper = ExchangeRateScraper(currency.symbol)
        exchange_rate_scraper.save_latest_exchange_rate()
        logger.info("Saved: %s" % currency.name)
