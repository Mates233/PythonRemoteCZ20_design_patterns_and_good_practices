"""
Úkol 1 - Builder

Představte si scénář objednávkového systému pizzerie, kde si zákazníci mohou přizpůsobit pizzu výběrem různých příloh,
typů kůrky a velikostí. Použijte vzor Builder a zapouzdřete konstrukci pizzy způsobem,
který udržuje proces konstrukce oddělený od reprezentace, aby bylo snadné přidávat nové možnosti bez úpravy stávajícího kódu.
"""


class Pizza:
    def __init__(self):
        self.topping = []
        self.dough = None
        self.size = None

    def __str__(self):
        return f"Pizza with toppings: {', '.join(self.topping)}, {self.dough} dough, and size {self.size}."


class PizzaBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._pizza = Pizza()

    def add_topping(self, topping):
        self._pizza.topping.append(topping)
        return self

    def add_dough(self, dough):
        self._pizza.dough = dough
        return self

    def add_size(self, size):
        self._pizza.size = size
        return self

    def build(self):
        if not self._pizza.dough:
            raise ValueError("Pizza must have dough.")
        built_pizza = self._pizza
        self.reset()  # Obnovení builderu pro další sestavení
        return built_pizza


# Create 3 pizzas with different toppings, doughs, and sizes
pizza_builder = PizzaBuilder()

margarita = pizza_builder.add_topping("mozzarella").add_topping("pomodoro").add_dough("thin").add_size("small").build()
hawaii = pizza_builder.add_topping("ham").add_topping("pineapple").add_topping("cheese").add_dough("regular").add_size("large").build()
bbq_chicken = pizza_builder.add_topping("chicken").add_topping("bbq sauce").add_topping("red onions").add_dough("thin").add_size("medium").build()


print(margarita)
print(hawaii)
print(bbq_chicken)
