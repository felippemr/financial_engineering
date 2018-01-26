

class TestExchangeRepr:
    pass


class TestExchangeStr:
    pass


class TestPositionHash:
    pass


class TestPositionRepr:
    pass


class TestPositionQuantity:
    pass


class TestPositionOpenedAt:
    def test_returns_false_if_greater(self):
        pass

    def test_returns_true_if_less(self):
        pass


class TestPositionPricePerUnity:
    pass


class TestPositionValue:
    pass


class TestPositionToDict:
    pass


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
