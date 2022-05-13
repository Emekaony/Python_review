class Calc:
    def __init__(self):
        pass
    
    @staticmethod
    def add(x, y):
        answer = x + y 
        print(answer)
    
    @staticmethod   
    def subtract(x, y):
        answer = x - y
        print(answer)
        
    @staticmethod
    def mult(x, y):
        answer = x * y
        print(answer)
        
    @staticmethod
    def div(x, y):
        answer = x / y
        print(answer)

tt = Calc()
# tt.mult(1, 2)
# tt.add(3, 4)

Calc.mult(3, 5)
Calc.div(3, 3)
