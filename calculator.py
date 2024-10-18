class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2 

    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        try:
            result = self.num1 / self.num2
            return result
        except ZeroDivisionError:
            return "Kļūda: Dalīšana ar nulli nav atļauta." 