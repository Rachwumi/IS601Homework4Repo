from History import Calculator_History
from calculation import Calculation
from decimal import Decimal


class Calculator:
    @staticmethod
    def _calculate(x:Decimal, y: Decimal, comp:str) -> Decimal:
            calc = Calculation(x, y, str)
            Calculator_History.addCalculation(calc)
            return calc.performCalculation()

    @staticmethod
    def add(x:Decimal, y:Decimal, str):
          return Calculator._calculate(x,y,'add')
    
    @staticmethod
    def subtract(x:Decimal, y:Decimal, str):
          return Calculator._calculate(x,y,'subtract')
    
    @staticmethod
    def divide(x:Decimal, y:Decimal, str):
          return Calculator._calculate(x,y,'divide')
    
    @staticmethod
    def multiply(x:Decimal, y:Decimal, str):
          return Calculator._calculate(x,y,'multiply')

