"""
编写项目的fixture
"""
from Interface.AddressInterface import AddressInterface
from Interface.CartInterface import CartInterface
from Interface.OrderInterface import OrderInterface
from Interface.MainFlowInterface import MainFlowInterface
import pytest


@pytest.fixture()
def cart():
    return CartInterface()


@pytest.fixture()
def order():
    return OrderInterface()


@pytest.fixture()
def address():
    return AddressInterface()

