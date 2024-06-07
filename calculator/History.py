from calculation import Calculation
from decimal import Decimal

class Calculator_History:
    Log: list[Calculation] = []
    size: 0

    @classmethod
    def addCalculation(cls, Calc):
        cls.size += 1
        return cls.log.append(Calc)
    
    @classmethod
    def getLastCalculation(cls):
        return cls.log[cls.size-1]
