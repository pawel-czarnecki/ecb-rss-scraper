from django.conf.urls import url

from .views import ExchangeRateListAPIView


urlpatterns = [
    url(r'^$', ExchangeRateListAPIView.as_view(), name='exchange_rate_list')
]
