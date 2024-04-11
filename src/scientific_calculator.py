from .custom_ex import IncorrectInputError, DivisionError


class Calculator:
    def add(self, *args: float) -> float:  # type: ignore
        return sum(args)
    
    def subtract(self, *args: float) -> float:
        try:
            result: float = args[0]
            for i in args[1:]:
                result -= i
            return result
        except TypeError:
            raise IncorrectInputError("Wrong Input")

    def multiply(self, *args: float):  # (1,2,3)
        try:
            result: float = 1
            for i in args:
                result *= i
            return result
        except TypeError:
            raise IncorrectInputError("Wrong Input")
        
    def divide(self, *args: float) -> float:
        try:
            result: float = args[0]
            for i in args[1:]:
                if not isinstance(i, (int, float)):
                    raise IncorrectInputError("Wrong Input")
                result /= i
            return result
        except ZeroDivisionError:
            raise  DivisionError("You can't divide by zero")
        except TypeError:
            raise IncorrectInputError("Wrong Input")

    def square(self, x: float) -> float:
        return x ** 2

    def cube(self, x: float) -> float:
        return x ** 3
