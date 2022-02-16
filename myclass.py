import math
import numbers


class MyClassError(Exception):
    pass
    # when the application error


class MyClass:
    def add(self, a, b):
        """Add two numbers."""
        self._check_operand(a)
        self._check_operand(b)
        return a + b

    def subtract(self, a, b):
        """Subtract two numbers."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide two numbers."""
        try:
            return a / b
        except ZeroDivisionError as ex:
            raise MyClassError("You can't divide by zero.") from ex

    def _check_operand(self, operand):
        """Check that the operand is a number."""
        if not isinstance(operand, numbers.Number):
            raise MyClassError(f'"{operand}" is not a number.')


if __name__ == "__main__":
    # ====================================== manual testing ======================================
    print("Let's calculate!")
    print("Press Ctrl+C to quit.")
    calculator = MyClass()
    operations = {
        "1": calculator.add,
        "2": calculator.subtract,
        "3": calculator.multiply,
        "4": calculator.divide,
    }
    while True:
        print("Pick a calculation:")

        for choice, operation in sorted(operations.items()):
            print(f"{choice}: {operation.__name__}")
        operation = input("What operation? ")
        if operation not in operations:
            print("Sorry, that's not a valid choice.")
            continue

        a = float(input("Select first operand: "))
        b = float(input("Select second operand: "))

        try:
            print("The result is: {}\n".format(operations[operation](a, b)))
        except MyClassError as error:
            print(error)
