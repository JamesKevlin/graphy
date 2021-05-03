

class ArithmeticService:

    def add(self, *args):  
        
        try:
            _sum = 0
            for arg in args:
                _sum +=arg

            return _sum
        except Exception:
            raise ArithmeticError

    def subtract(self, *args):
        try:
            _diff = args[0]
            for arg in args[1:]:
                _diff -=arg

            return _diff
        except Exception:
            raise ArithmeticError

    def multiply(self, *args):
        try:
            _diff = args[0]
            for arg in args[1:]:
                _diff *= arg

            return _diff
        except Exception:
            raise ArithmeticError

    def divide(self, *args):
        try:
            _diff = args[0]
            for arg in args[1:]:
                _diff /= arg

            return _diff
        except Exception:
            
            raise ArithmeticError

    # def parentheses

    def exponents(self, *args):
        try:
           
            return (args[0] ** args[1])
        except Exception:
            raise ArithmeticError


    # TODO
    # def sqrt