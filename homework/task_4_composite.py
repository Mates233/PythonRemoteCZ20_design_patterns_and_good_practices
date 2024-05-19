""""
Úkol

1.	Definujte třídu Component s metodami pro přidávání/odebírání komponent a pro provádění operací.
2.	Implementujte třídu Employee, která rozšiřuje třídu Component.
3.	Implementujte třídu Department, která rozšiřuje třídu Component a spravuje kolekci komponent (zaměstnanců a dílčích oddělení).
4.	Napište klientský kód pro vytvoření organizační struktury a provádění operací nad ní.

Kroky

1.	Implementujte třídu Zaměstnanec.
2.	Implementujte třídu Department.
3.  Implementujte přidání/odebrání zaměstnanece a departmentu v main
"""

from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def add(self, component):
        pass

    @abstractmethod
    def remove(self, component):
        pass

    @abstractmethod
    def display(self, indent=0):
        pass

    @abstractmethod
    def get_salary(self):
        pass


class Employee(Component):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def add(self, component):
        pass

    def remove(self, component):
        pass

    def display(self, indent=0):
        pass

    def get_salary(self):
        pass


class Department(Component):
    def __init__(self, name):
        self.name = name
        self._components = []

    def add(self, component):
        pass

    def remove(self, component):
        pass

    def display(self, indent=0):
        pass

    def get_salary(self):
        pass


def main():
    # Create employees
    emp1 = Employee("Alice", 10000)
    emp2 = Employee("Bob", 15000)
    emp3 = Employee("Charlie", 20000)
    emp4 = Employee("Diana", 25000)

    dept1 = Department("HR")
    dept2 = Department("Engineering")
    # TODO pridat zamestnance do oddeleni

    company = Department("Company")

    # TODO pridat zamenstance do spolecnosti
    company.display()

    print(f"Total Salary: {company.get_salary()}")


if __name__ == '__main__':
    main()
