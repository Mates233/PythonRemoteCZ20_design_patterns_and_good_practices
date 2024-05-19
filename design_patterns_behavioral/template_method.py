"""
Vzor Template Method umožňuje definovat schéma algoritmu.
Takový rámec má sadu pohyblivých prvků – neimplementovaných metod, které lze přepsat.
Tyto části by měly být použity k definování algoritmu.
"""

from abc import ABC, abstractmethod


class Beverage(ABC):
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Boiling water")

    @abstractmethod
    def brew(self):
        pass

    def pour_in_cup(self):
        print("Pouring into cup")

    @abstractmethod
    def add_condiments(self):
        pass


class Tea(Beverage):
    def brew(self):
        print("Steeping the tea")

    def add_condiments(self):
        print("Adding lemon")


class Coffee(Beverage):
    def brew(self):
        print("Dripping coffee through filter")

    def add_condiments(self):
        print("Adding sugar and milk")


def main():
    tea = Tea()
    coffee = Coffee()

    print("Making tea:")
    tea.prepare_recipe()

    print("\nMaking coffee:")
    coffee.prepare_recipe()


if __name__ == "__main__":
    main()
