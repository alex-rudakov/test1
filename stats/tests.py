from datetime import date
from decimal import Decimal

import pytest

from stats.models import Currency, Rate
from stats.services import get_stats, load_data


@pytest.mark.django_db
def test_basic_iteractions():
    start_count = Currency.objects.count()

    cur = Currency(name="Fantiki")
    cur.save()

    assert Currency.objects.count() == start_count + 1


@pytest.mark.django_db
def test_stats():
    cur = Currency(name="BTC")
    cur.save()

    Rate(currency=cur, date=date(1967, 8, 3), rate=23, volume=1000).save()
    Rate(currency=cur, date=date(1967, 8, 4), rate=18, volume=3000).save()
    Rate(currency=cur, date=date(1967, 8, 5), rate=150, volume=2000).save()

    stats = get_stats(name="BTC", from_date=date(1967, 8, 5), last_days=3)

    assert isinstance(stats, dict)
    assert stats.get('last_rate') == 150
    assert stats.get('average_volume') == 2000


@pytest.mark.django_db
def test_stats_no_data():
    cur = Currency(name="BTC")
    cur.save()

    stats = get_stats(name="BTC", from_date=date(1967, 8, 5), last_days=3)

    assert isinstance(stats, dict)
    assert stats.get('last_rate') is None
    assert stats.get('average_volume') is None


@pytest.mark.django_db
def test_stats_no_currency():
    stats = get_stats(name="Lololo", from_date=date(1967, 8, 5), last_days=3)

    assert stats is None


@pytest.mark.django_db
def test_parse_data():
    data = [
        [
            1569024000000,
            10197.99421167,
            10082,
            10199,
            9942.9,
            1410.34036069
        ],
        [
            1568937600000,
            10300.768691,
            10197,
            10340,
            10104,
            2514.16347485
        ],
        [ # testing this
            1568851200000,
            10184.97069252,
            10301,
            10487,
            9655,
            9766.20759473
        ],
        [
            1568764800000,
            10216,
            10185,
            10278,
            10111,
            3339.17191254
        ],
    ]

    load_data(name="LOLO", data=data)

    assert Currency.objects.filter(name="LOLO").exists()

    assert Rate.objects.filter(currency__name="LOLO").count() == 4

    rate = Rate.objects.filter(currency__name="LOLO").order_by("-date")[2]

    assert rate.date == date(2019, 9, 19)
    assert rate.rate == 10301
    assert rate.volume == Decimal('9766.20759473')



