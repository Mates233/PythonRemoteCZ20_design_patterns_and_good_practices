"""
Decorator
Účel: přidání nové funkce ke stávajícímu objektu

Vlastnosti:

běžné rozhraní dekoratérů
vždy volá původní metodu objektu
dekorátory lze aplikovat v libovolném pořadí
bez využití dědičnosti
jednoduchá implementace
Decorator - struktura
dekorovaný objekt
běžné rozhraní dekoratérů / základní třída
implementace dekorátorů
umožňuje přidat objektům nové chování umístěním těchto objektů do speciálních obalových objektů,
 které obsahují dané chování

 ! Dekorator pattern (extenduje objekty dynamicky) != decorator v Pythonu (extenduje funkce a metody)
"""

from abc import ABC, abstractmethod


class Operation(ABC):                           # komponent interface
    @abstractmethod
    def execute(self, data):
        pass


class SimpleOperation(Operation):               # komponent
    def execute(self, data):
        return f"Processing {data}"


class OperationDecorator(Operation):            # decorator zakladni class
    def __init__(self, operation):
        self._operation = operation

    def execute(self, data):
        return self._operation.execute(data)


class LoggingDecorator(OperationDecorator):     # konkretni dekorator
    def execute(self, data):
        result = self._operation.execute(data)
        self.log(data, result)
        return result

    def log(self, data, result):
        print(f"Logging: Executed operation on {data} with result: {result}")


class AuthenticationDecorator(OperationDecorator):  # konkretni dekorator
    def execute(self, data):
        if self.authenticate(data):
            return self._operation.execute(data)
        else:
            return "Authentication failed"

    def authenticate(self, data):
        # Dummy authentication logic
        return data == "authorized data"


def main():
    # Create a simple operation
    simple_operation = SimpleOperation()

    # Decorate the operation with logging
    logged_operation = LoggingDecorator(simple_operation)

    logged_operation.execute("logged data")

    # Optionally, decorate with authentication as well
    authenticated_and_logged_operation = AuthenticationDecorator(logged_operation)

    # Execute the decorated operation
    result = authenticated_and_logged_operation.execute("authorized data")
    print(result)

    # Execute with unauthorized data
    result = authenticated_and_logged_operation.execute("unauthorized1 data")
    print(result)

if __name__ == "__main__":
    main()
