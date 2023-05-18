import app
import math

class InvalidPermissions(Exception):
    pass


class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    def substract(self, x, y):
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('User has no permissions')

        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        return x ** y


     # NEW -> Raíz cuadrada
    def sqrt(self, x):
        self.check_types_one_parameter(x)
        if x <= 0:
            raise TypeError("La raiz cuadrada de un número menor o igual a 0 no existe")
        
        return math.sqrt(x)


    # NEW -> Logaritmo en base 10
    def log(self, x):
        self.check_types_one_parameter(x)
        if x <= 0:
            raise TypeError("El logaritmo en base 10 de un número menor o igual a 0 no existe")
        
        return math.log10(x)


    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")
        
    # NEW -> Only one parameter  
    def check_types_one_parameter(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Parameter must be number")


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)
