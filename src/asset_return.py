
def calculate_rate_of_return(
    current_price: float, future_price: float,
) -> float:
    return round((future_price - current_price) / current_price, 1)
