from datetime import timedelta
from decimal import Decimal
import pytest

from src.portfolio import Exchange, Position


class TestExchangeInit:
    def test_exchange_needs_a_name_to_exists(self):
        with pytest.raises(TypeError):
            Exchange()


class TestExchangeRepr:
    def test_repr_returns_name(self):
        assert repr(Exchange(name='NYSE')) == '<Exchange: name=NYSE>'


class TestExchangeStr:
    def test_str_returns_name(self):
        assert str(Exchange(name='NYSE')) == 'NYSE'


class TestPositionInit:
    def test_position_needs_opened_at_quantity_price_per_unit_to_exists(self):
        with pytest.raises(
            TypeError,
            match="missing 3 required positional arguments:"
                " 'opened_at', 'quantity', and"
        ):
            Position()


class TestPositionId:
    def test_id_does_not_repeat(self, position, another_position):
        assert position.id != another_position.id


class TestPositionHash:
    def position_hash_returns_id(self, position):
        assert hash(position) == position.id


class TestPositionRepr:
    def test_repr_returns_id_opened_quantity_price(self, position, as_of):
        assert repr(position) == '<Position: id=2, opened={}, quantity=20, price=10>'.format(
            as_of
        )


class TestPositionProperties:
    @pytest.mark.parametrize('_property,_private_attr', [
        ('id', '_id'),
        ('quantity', '_quantity'),
        ('price_per_unit', '_price_per_unit'),
        ('closed_at', '_closed_at'),
    ])
    def test_property_returns_private_attribute(self, _property, _private_attr, position):
        assert getattr(position, _property) is getattr(position, _private_attr)

    def test_position_close_at_throws_value_error_if_value_eq_opened_at(self, position, as_of):
        with pytest.raises(ValueError, match="Can't close in the past!"):
            position.closed_at = as_of

    def test_position_close_at_throws_value_error_if_value_lt_opened_at(self, position, as_of):
        with pytest.raises(ValueError, match="Can't close in the past!"):
            position.closed_at = as_of - timedelta(microseconds=1)


class TestPositionOpenedAsOf:
    def test_returns_false_if_closed_date_lt_than_param(
        self, position, as_of
    ):
        position.closed_at = as_of + timedelta(microseconds=1)
        future_date = as_of + timedelta(microseconds=2)
        assert position.opened_as_of(future_date) is False

    def test_returns_false_if_closed_date_eq_param(
        self, position, as_of
    ):
        future_date = as_of + timedelta(microseconds=1)
        position.closed_at = future_date
        assert position.opened_as_of(future_date) is False

    def test_returns_true_if_closed_date_gt_than_param_and_opened_gt_param(
        self, position, as_of
    ):
        position.closed_at = as_of + timedelta(microseconds=1)
        assert position.opened_as_of(as_of) is True

    def test_returns_true_if_closed_date_gt_param_and_opened_eq_param(
        self, position, as_of
    ):
        position.closed_at = as_of + timedelta(microseconds=1)
        assert position.opened_as_of(as_of) is True


class TestPositionValue:
    def test_if_returns_quantity_times_price_per_unit(self, position):
        assert position.value == Decimal(200)


class TestPositionToDict:
    def test_if_returns_dict_with_id_as_the_key_and_self_value(
        self, position
    ):
        assert position.to_dict() == {position.id: position}


class TestAssetIsBorg:
    pass


class TestAssetHash:
    pass


class TestAssetRepr:
    pass


class TestAssetId:
    pass


class TestAssetAddPosition:
    pass


class TestAssetToDict:
    pass


class TestAssetPositions:
    pass


class TestAssetGetPrice:
    pass


class TestAssetValue:
    def test_value_error_if_both(self):
        pass

    def test_calculate_initial_does_not_call_get_price(self):
        pass

    def test_calculate_as_of_does_calls_get_price(self):
        pass

    def test_returns_sum_of_positions_if_initial(self):
        pass

    def test_return_sum_of_positions_if_as_of(self):
        pass


class TestPortfolioAddAsset:
    def test_add_if_does_not_exist(self):
        pass

    def test_do_not_add_if_exists(self):
        pass


class TestPortfolioAssets:
    pass


class TestPortfolioValue:
    pass


class TestPortfolioRateOfReturn:
    pass
