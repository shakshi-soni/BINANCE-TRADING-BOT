import click

def validate_inputs(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    """Validates CLI inputs and raises standard Click usage errors if rules are broken."""

    if side.upper() not in ["BUY", "SELL"]:
        raise click.BadParameter("Side must be either 'BUY' or 'SELL'.")

    if order_type.upper() not in ["MARKET", "LIMIT"]:
        raise click.BadParameter("Order type must be either 'MARKET' or 'LIMIT'.")

    if quantity <= 0:
        raise click.BadParameter("Quantity must be a positive number greater than 0.")

    if order_type.upper() == "LIMIT":
        if price is None or price <= 0:
            raise click.BadParameter("Price is required and must be greater than 0 for LIMIT orders.")
            
    return {
        "symbol": symbol.upper(),
        "side": side.upper(),
        "order_type": order_type.upper(),
        "quantity": quantity,
        "price": price
    }