import requests
from django.core.management.base import BaseCommand, CommandError

from stats.services import load_data


class Command(BaseCommand):
    help = 'Fetch currency stats from data source'

    def add_arguments(self, parser):
        parser.add_argument('currencies', nargs='+', type=str)

    def handle(self, *args, **options):
        for currency in options['currencies']:
            print(f'Fetching {currency}')
            data = requests.get(f'https://api-pub.bitfinex.com/v2/candles/trade:1D:t{currency}USD/hist').json()
            print(f'Parsing {currency}')
            load_data(name=currency, data=data[:10])

        print('Done')
