from rest_framework import serializers
from stats.models import Currency, Rate


class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = ['id', 'name']


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = ['id', 'currency', 'date', 'rate', 'volume']


index = {
    Currency: {
        '_': CurrencySerializer,
    },

    Rate: {
        '_': RateSerializer,
    },
}
