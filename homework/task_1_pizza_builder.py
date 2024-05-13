"""
Úkol 1 - Builder

Představte si scénář objednávkového systému pizzerie, kde si zákazníci mohou přizpůsobit pizzu výběrem různých příloh,
typů kůrky a velikostí. Použijte vzor Builder a zapouzdřete konstrukci pizzy způsobem,
který udržuje proces konstrukce oddělený od reprezentace, aby bylo snadné přidávat nové možnosti bez úpravy stávajícího kódu.
"""


class Pizza:
    def __init__(self):
        self.topping: list
        self.dough = None
        self.size = None

    def __str__(self):
        return f"Pizza with {self.topping}, {self.dough} dough and size {self.size}."


class PizzaBuilder:
    def __init__(self):
        self._pizza = Pizza()

    def add_topping(self):
        pass
        return self

    def add_dough(self):
        pass
        return self

    def build(self):
        return self._pizza


### Vyrobit 3 pizzy s různými příchutěmi, kůrkami a velikostmi
pizza_builder = PizzaBuilder()
margarita = pizza_builder.add_topping("mozzarella, pomodoro").add_dough("thin").add_size("small").build()
