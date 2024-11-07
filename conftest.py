import pytest
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods


@pytest.fixture()
def courier():
    return CourierMethods()

@pytest.fixture()
def order():
    return OrderMethods()








