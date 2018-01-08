from src.asset_return import calculate_rate_of_return


class TestCalculateRateOfReturn:

    def test_when_current_price_is_equal_to_future_price_rate_is_zero(self):
        assert calculate_rate_of_return(10.0, 10.0) == 0.0

    def test_when_current_price_is_greater_than_future_price_rate_is_positive(self):
        assert calculate_rate_of_return(10.0, 11.0) == 0.1

    def test_when_current_price_is_lesser_than_future_price_rate_is_negative(self):
        assert calculate_rate_of_return(11.0, 10.0) == -0.1
