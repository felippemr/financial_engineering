from datetime import datetime
from decimal import Decimal
import pytest
from src.portfolio import Position

def _build_position(quantity, price_per_unit, as_of):
    return Position(
        opened_at=as_of, quantity=quantity, price_per_unit=price_per_unit
    )

@pytest.fixture
def as_of():
    return datetime(
        year=2017, month=1, day=1, hour=1,
        minute=0, second=0, microsecond=0
    )


@pytest.fixture
def position(as_of):
    return _build_position(Decimal(20), Decimal(10), as_of)


@pytest.fixture
def another_position(as_of):
    return _build_position(Decimal(30), Decimal(40), as_of)
