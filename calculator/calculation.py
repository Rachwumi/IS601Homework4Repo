from arithematic import add, subtract, divide, multiply
from decimal import Decimal
from string import str

class Calculation:
    def __init__(self, x: Decimal, y: Decimal, comp:str):
        self.x = x
        self.y = y
        self.comp = comp

@classmethod
def performCalculation(self):
    if self.comp == 'add':
        return add(self.x, self.y)
    elif self.comp == 'subtract':
        return subtract(self.x, self.y)
    elif self.comp == 'mulitply':
        return multiply(self.x, self.y)
    else:
        return divide(self.x, self.y)



