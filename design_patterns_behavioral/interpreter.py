"""
Předpokládejme:

v terminálu v shellu bash spustíme příkaz ls -ltr | grep -i sda
v konzoli python spustíme příkaz 3 ** 3 + 1
v konzoli jshell spustíme příkaz Math.abs(Math.pow(2, 3)).
Každý z výše uvedených příkladů bere jako vstup nějakou informaci, obvykle ve formě řetězce.
Poté jsou tyto znaky interpretovány určitým dohodnutým způsobem (tj. v závislosti na smlouvě a možnostech technologie)
a poskytují konkrétní výsledek. Toto chování popisuje použití vzoru interpret.

Design
Abychom mohli použít vzor, potřebujeme následující prvky:

společné rozhraní, které má metodu pro interpretaci určitého objektu. Tento objekt často nazýváme kontext ( context)
implementace rozhraní, která mohou interpretovat kontext různými způsoby
"""

class MathOperationAplier:
    def apply(self, math_operation, first, second):
        if math_operation == '+':
            return first + second
        elif math_operation == '-':
            return first - second
        elif math_operation == '*':
            return first * second
        elif math_operation == '/':
            return first / second
        elif math_operation == '**':
            return first ** second
        else:
            raise ArithmeticError()


class Interpreter:
    def interpret(self, context):
        pass


class PythonStyleWithoutOrderMathOperationsInterpreter(Interpreter):
    def __init__(self, math_operation_applier):
        self._math_operation_applier = math_operation_applier

    def interpret(self, context):
        split_data = context.strip().split()
        if len(split_data) % 2 == 0:
            raise ArithmeticError()

        value = float(split_data[0])
        for i in range(1, len(split_data), 2):
            value = self._math_operation_applier.apply(split_data[i], value, float(split_data[i + 1]))
        return value


def main():
    math_operation_applier = MathOperationAplier()
    interpreter = PythonStyleWithoutOrderMathOperationsInterpreter(math_operation_applier)

    calculation = input('Choose a math operation: ')

    value = interpreter.interpret(calculation)

    print(value)


if __name__ == '__main__':
    main()