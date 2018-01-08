from src.asset_return import calculate_future_asset_return


class TestFutureAssetReturn:

    def test_when_current_price_per_share_is_equal_to_bought_at_return_is_zero(self):
        assert calculate_future_asset_return(10.0, 10.0) == 0.0

    def test_when_current_price_per_share_is_greater_than_to_bought_at_return_is_positive(self):
        assert calculate_future_asset_return(11.0, 10.0) == 0.1

    def test_when_current_price_per_share_is_lesser_than_to_bought_at_return_is_negative(self):
        assert calculate_future_asset_return(10.0, 11.0) == -0.1
