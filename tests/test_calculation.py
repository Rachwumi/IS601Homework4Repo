'''My Calculcation Test'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation

@pytest.mark.parametrize("int1, int2, operation, expected", [
    (Decimal('20'), Decimal('36'), 'add', Decimal('56')),  # Test addition
    (Decimal('4'), Decimal('5'), 'subtract', Decimal('-1')),  # Test subtraction
    (Decimal('100'), Decimal('23'), 'multiply', Decimal('2300')),  # Test multiplication
    (Decimal('81'), Decimal('9'), 'divide', Decimal('9'))  # Test division
])

def test_performcalc(int1,int2, operation, expected):
    '''
        Testing the perfomCalculation() method in the calculation class
    '''
    c = Calculation(int1,int2,operation)
    assert c.performCalculation() == expected,f"Failed {operation} operation with {int1} and {int2}"
    