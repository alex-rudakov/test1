from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from stats.services import get_stats
from .serializers import CurrencySerializer, RateSerializer
from stats.models import Currency, Rate
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class CurrencyViewSet(ReadOnlyModelViewSet):
    """
    Currency API
    """

    filter_fields = ['id', 'name']
    serializer_class = CurrencySerializer

    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]

    def get_queryset(self):
        return Currency.objects.all()


class StatsViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        return Response(get_stats(name=pk))

