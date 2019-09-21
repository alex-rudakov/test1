from datetime import date, timedelta, datetime
from decimal import Decimal
from typing import List

from django.db.models import Avg
from django.utils.timezone import now

from stats.models import Rate, Currency


def get_stats(name: str, from_date: date = now(), last_days: int = 10):
    """
    Return last stats for given currency. Stats inlude last rate & average volume for specified period.

    :param name:
    :param from_date:
    :param last_days:
    :return: dict|None {last_rate:decimal, average_volume:decimal}
    """
    try:
        currency = Currency.objects.get(name=name)
    except Currency.DoesNotExist:
        return None

    qs = Rate.objects.filter(
        currency=currency,
        date__lte=from_date,
        date__gt=from_date - timedelta(days=last_days)
    ).order_by('-date')

    if qs.count() == 0:
        return {
            'last_rate': None,
            'average_volume': None,
        }

    return {
        **{"last_rate": qs.order_by('-date').values('rate')[0]['rate']},
        **qs.aggregate(average_volume=Avg('volume'))
    }


def load_data(name: str, data: List[List[int]]):
    currency, created = Currency.objects.get_or_create(name=name)

    for line in data:
        rate, created = Rate.objects.get_or_create(
            currency=currency,
            date=datetime.fromtimestamp(line[0] / 1000).date()
        )
        rate.rate = Decimal(line[2])
        rate.volume = Decimal(line[5])

        rate.save()

