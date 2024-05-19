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
        print(' ' * indent + f"Employee: {self.name}, Salary: {self.salary}")

    def get_salary(self):
        return self.salary


class Department(Component):
    def __init__(self, name):
        self.name = name
        self._components = []

    def add(self, component):
        self._components.append(component)

    def remove(self, component):
        self._components.remove(component)

    def display(self, indent=0):
        print(' ' * indent + f"Department: {self.name}")
        for component in self._components:
            component.display(indent + 4)

    def get_salary(self):
        total_salary = 0
        for component in self._components:
            total_salary += component.get_salary()
        return total_salary


def main():
    # Create employees
    emp1 = Employee("Alice", 10000)
    emp2 = Employee("Bob", 15000)
    emp3 = Employee("Charlie", 20000)
    emp4 = Employee("Diana", 25000)

    # Dep with 2 emp
    dept1 = Department("HR")
    dept1.add(emp1)
    dept1.add(emp2)

    # Dep with 2 emp
    dept2 = Department("Engineering")
    dept2.add(emp3)
    dept2.add(emp4)

    # Company dep
    company = Department("Company")
    company.add(dept1)
    company.add(dept2)

    # $$$
    company.display()
    print(f"Total Salary: {company.get_salary()}")

if __name__ == '__main__':
    main()
