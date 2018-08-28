from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=30)
    symbol = models.CharField(max_length=3, unique=True, null=False)

    def __str__(self):
        return '%s (%s)' % (self.name, self.symbol)


class ExchangeRate(models.Model):
    currency = models.ForeignKey(Currency)
    rate = models.DecimalField(max_digits=6, decimal_places=4, default=0.0, null=False)
    date = models.DateTimeField(null=False)

    def __str__(self):
        return '%s %s (%s)' % (self.rate, self.currency.symbol, self.date.strftime('%d %B %Y, %H:%M'))
