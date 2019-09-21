from django.conf.urls import url, include
from rest_framework import routers
from .views_rest import CurrencyViewSet, StatsViewSet

router = routers.DefaultRouter()

router.register(r'currency', CurrencyViewSet, r'currency')

router.register(r'stats', StatsViewSet, r'stats')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]
