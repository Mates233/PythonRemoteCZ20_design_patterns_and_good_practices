"""
Demeterův zákon (The Law Of Demeter), známý také jako princip nejmenšího množství znalostí,
který podporuje volné propojení v softwarových systémech. Nařizuje, že daný objekt by měl
komunikovat pouze se svými bezprostředními spolupracovníky a neměl by „pronikat“ přes více vrstev objektů.

Konkrétně by měl objekt volat pouze metody:
1.	sám sobě
2.	svých přímých atributů
3.	Objekty vytvořené v rámci jeho metod
4.	Objekty předávané jako argumenty jeho metodám
5.	Její bezprostřední součásti

Dodržováním této zásady omezíte závislosti mezi třídami, což usnadňuje údržbu kódu a snižuje náchylnost k chybám.
Zapouzdření podporuje lepší modularitu a zvyšuje robustnost a čitelnost kódu.
"""


"""
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def get_horsepower(self):
        return self.horsepower

class Car:
    def __init__(self, engine):
        self.engine = engine

class Person:
    def __init__(self, car):
        self.car = car

    def get_car_engine_horsepower(self):
        return self.car.engine.get_horsepower()  # Porušení: Příliš mnoho teček


engine = Engine(150)
car = Car(engine)
person = Person(car)

print(person.get_car_engine_horsepower()) 
"""


class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def get_horsepower(self):
        return self.horsepower


class Car:
    def __init__(self, engine):
        self.engine = engine

    def get_engine_horsepower(self):
        return self.engine.get_horsepower()


class Person:
    def __init__(self, car):
        self.car = car

    def get_car_engine_horsepower(self):
        return self.car.get_engine_horsepower()  # iba jedna tečka



#engine = Engine(150)
#car = Car(engine)
#person = Person(car)
#
#print(person.get_car_engine_horsepower())