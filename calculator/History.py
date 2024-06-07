from calculator.calculation import Calculation as calc

class Calculator_History:
    log: list[calc] = []
    size = 0

    @classmethod
    def addCalculation(cls, Calc):
        cls.size += 1
        return cls.log.append(Calc)
    
    @classmethod
    def getLastCalculation(cls):
        return cls.log[cls.size-1]
