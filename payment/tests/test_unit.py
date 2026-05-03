"""Unit test: poslovna logika u izolaciji, eksterna zavisnost mokovana."""
from unittest.mock import MagicMock


def test_order_total_calculation():
    inventory_product = MagicMock()
    inventory_product.price = 100.0
    quantity = 2

    fee = 0.2 * inventory_product.price
    total = 1.2 * inventory_product.price * quantity

    assert fee == 20.0
    assert total == 240.0
