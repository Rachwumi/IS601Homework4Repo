'''My Calculcation Test'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation

def test_performcalc(int1,int2, operation, expected):
    '''
        Testing the perfomCalculation() method in the calculation class
    '''
    c = Calculation(int1,int2,operation)
    assert c.performCalculation() == expected,f"Failed {operation} operation with {int1} and {int2}"
    