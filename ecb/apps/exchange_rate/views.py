from rest_framework.generics import ListAPIView

from .models import ExchangeRate
from .serializers import ExchangeRateSerializer


class ExchangeRateListAPIView(ListAPIView):
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer
