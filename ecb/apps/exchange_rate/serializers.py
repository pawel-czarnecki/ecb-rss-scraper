from rest_framework.serializers import ModelSerializer

from .models import ExchangeRate


class ExchangeRateSerializer(ModelSerializer):
    class Meta:
        depth = 1
        model = ExchangeRate
        fields = '__all__'
