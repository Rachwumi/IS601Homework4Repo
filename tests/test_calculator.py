'''My Calculator Test'''

from decimal import Decimal
from calculator import Calculator

def test_addition():
    '''Test that addition function works '''    
    assert Calculator.add(2, 2, 'add') == Decimal(4)

def test_subtraction():
    '''Test that subtraction function works '''    
    assert Calculator.subtract(2, 2, 'subtract') == Decimal(0)

def test_multiplication():
    '''Test that multiplication function works '''    
    assert Calculator.multiply(2, 2, 'multiply') == Decimal(4)

def test_division():
    '''Test that division function works '''    
    assert Calculator.divide(2, 2, 'divide') == Decimal(1) 

def test_divisionFailure():
    '''Test that division function works '''    
    assert Calculator.subtract(2, 2, 'divide') == Decimal(0)
