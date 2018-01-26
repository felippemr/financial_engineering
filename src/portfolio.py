from itertools import count
from typing import Dict, Iterable
from random import randint
from datetime import datetime, timedelta
from decimal import Decimal

GLOBAL_IDENTITY = count()


class Exchange:
    def __init__(self, name):
        self._name = name

    def __repr__(self):
        return '<Exchange: name={}>'.format(self._name)

    def __str__(self):
        return self._name


class Position:

    def __init__(
        self, opened_at:datetime, quantity: Decimal, price_per_unit: Decimal,
    ):
        self._id = next(GLOBAL_IDENTITY)
        self._opened_at = opened_at
        self._quantity = quantity
        self._price_per_unit = price_per_unit

    def __hash__(self):
        return self._id

    def __repr__(self):
        return '<Position: id={}, opened={}, quantity={}, price={}>'.format(
            self._id, self._opened_at, self._quantity, self._price_per_unit
        )

    @property
    def quantity(self) -> Decimal:
        return self._quantity

    def opened_at(self, as_of: datetime) -> bool:
        return self._opened_at <= as_of

    @property
    def price_per_unit(self):
        return self._price_per_unit

    @property
    def value(self) -> Decimal:
        return self._quantity * self._price_per_unit

    def to_dict(self) -> Dict[int, 'Position']:
        return {self._id: self}


class Asset:
    __instances = {}

    def __init__(self, exchange: Exchange, symbol: str, data_provider):
        try:
            self.__dict__ = self.__instances['{}-{}'.format(symbol, exchange)].__dict__
        except KeyError:
            self._id = next(GLOBAL_IDENTITY)
            self._exchange = exchange
            self._symbol = symbol

            self._positions = {}
            self._data_provider = data_provider

            self.__instances['{}-{}'.format(symbol, exchange)] = self

    def __hash__(self):
        return self._id

    def __repr__(self):
        return '<Asset: id={}, exchange={}, symbol={}>'.format(
            self._id, self._exchange, self._symbol
        )

    @property
    def id(self):
        return self._id

    def add_position(self, position: Position):
        self._positions.update(position.to_dict())

    def to_dict(self) -> Dict[int, 'Asset']:
        return {self._id: self}

    @property
    def positions(self) -> Iterable[Position]:
        return self._positions.values()

    def get_price(self, as_of: datetime) -> Decimal:
        return self._data_provider.get_price_for_asset(
            asset=self, as_of=as_of
        )

    def value(self, as_of: datetime=None, initial: bool=False) -> Decimal:
        if as_of and initial:
            raise ValueError(
                "Can't use as_of and initial together!"
            )

        price_as_of_date_time = 0
        if as_of:
            price_as_of_date_time = self.get_price(as_of=as_of)

        total = Decimal(0)
        for position in self.positions:
            if initial:
                total += position.value
            elif position.opened_at(as_of):
                total += (
                    position.quantity
                    * price_as_of_date_time
                )

        return total


class Portfolio:

    def __init__(self):
        self._assets = {}

    def add_asset(self, asset: Asset):
        if asset.id not in self.assets:
            self._assets.update(asset.to_dict())

    @property
    def assets(self):
        return self._assets.values()

    def value(self, as_of: datetime=None, initial: bool=False):
        return sum(
            asset.value(as_of=as_of, initial=initial)
            for asset in self.assets
        )

    def rate_of_return(self, as_of: datetime):
        initial_value = self.value(initial=True)
        value_as_of = self.value(as_of=as_of)

        return (value_as_of - initial_value) / initial_value


class DummyDataProvider:

    def get_price_for_asset(self, asset: Asset, as_of: datetime):
        return randint(0, 1000)


def build_scenario():
    exchange = Exchange(name='NYSE')
    print(Exchange)
    portfolio = Portfolio()
    data_provider = DummyDataProvider()

    as_of = datetime(
        year=2017, month=1, day=1, hour=1, minute=0, second=0, microsecond=0
    )
    raw_data = [
        ('AAPL', Decimal(200), as_of + timedelta(days=30), Decimal(100)),
        ('AAPL', Decimal(400), as_of + timedelta(days=32), Decimal(90)),
        ('MSFT', Decimal(50), as_of + timedelta(days=30), Decimal(90)),
    ]


    for item in raw_data:
        symbol, quantity, opened, price = item
        asset = Asset(exchange, symbol=symbol, data_provider=data_provider)
        print(asset)

        position = Position(
            quantity=quantity, opened_at=opened, price_per_unit=price
        )
        print(position)

        asset.add_position(position)
        print(asset.positions)

        portfolio.add_asset(asset)
        print(portfolio.assets)

    return portfolio





