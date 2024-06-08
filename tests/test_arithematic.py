'''My Arithematic Test'''
from decimal import Decimal
import pytest
from calculator.arithematic import add, subtract, multiply, divide

@pytest.mark.parametrize("int1, int2", [
    (Decimal('20'), Decimal('36')),
    (Decimal('4'), Decimal('5')),
    (Decimal('100'), Decimal('23')),
    (Decimal('81'), Decimal('9'))
])

def test_add(int1, int2):
    ''' Testing the addition arithematic'''
    expected = int1 + int2
    assert add(int1, int2) == expected, f"Failed the addition with {int1} and {int2}"

@pytest.mark.parametrize("int1, int2", [
    (Decimal('20'), Decimal('36')),
    (Decimal('4'), Decimal('5')),
    (Decimal('100'), Decimal('23')),
    (Decimal('81'), Decimal('9'))
])
def test_subtract(int1, int2):
    ''' Testing the subtractarithematic'''
    expected = int1 - int2
    assert subtract(int1, int2) == expected, f"Failed the subtract with {int1} and {int2}"

@pytest.mark.parametrize("int1, int2", [
    (Decimal('20'), Decimal('36')),
    (Decimal('4'), Decimal('5')),
    (Decimal('100'), Decimal('23')),
    (Decimal('81'), Decimal('9'))
])
def test_multiply(int1, int2):
    ''' Testing the multiply arithematic'''
    expected = int1 * int2
    assert multiply(int1, int2) == expected, f"Failed the multiply with {int1} and {int2}"

@pytest.mark.parametrize("int1, int2", [
    (Decimal('20'), Decimal('36')),
    (Decimal('4'), Decimal('5')),
    (Decimal('100'), Decimal('23')),
    (Decimal('81'), Decimal('9'))
])
def test_divide(int1, int2):
    ''' Testing the divide arithematic'''
    expected = int1 / int2
    assert divide(int1, int2) == expected, f"Failed the divide with {int1} and {int2}"

def test_dividefail():
    ''' Testing the divide fail arithematic'''
    with pytest.raises(Exception, match="You can not divide by zero"):
        assert divide(Decimal('10'), Decimal('0'))
