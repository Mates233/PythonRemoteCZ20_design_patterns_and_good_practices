"""
Definice:
Rozhraní definuje smlouvu pro třídy a specifikuje sadu metod, které musí být implementovány, aniž by poskytovalo
podrobnosti o implementaci. Rozhraní umožňují polymorfismus a umožňují zaměnitelné použití různých tříd,
 pokud implementují stejné rozhraní.

Klíčové body:

- Žádná implementace: Pouze deklarace metod.
- Vícenásobná dědičnost: Třída může implementovat více rozhraní.
- Polymorfismus: Umožňuje zacházet s objekty různých tříd jednotně.

Abstraktní třídy

Definice:
Abstraktní třída je třída, která nemůže být sama instancována a je určena pro podtřídy. Může obsahovat jak
abstraktní metody (bez implementace), tak konkrétní metody (s implementací), čímž poskytuje společný
základ pro příbuzné třídy.

Klíčové body:

- Částečná implementace: Obsahuje jak abstraktní, tak konkrétní metody.
- Jednoduchá dědičnost: Třída může dědit pouze z jedné abstraktní třídy.
- Sdílený kód: Usnadňuje opakované použití kódu mezi příbuznými třídami.

Rozdíly mezi rozhraními a abstraktními třídami

1.	Účel:
- Rozhraní: Definovat smlouvu pro implementaci metody.
- Abstraktní třídy: Poskytnout společný základ se sdíleným kódem a chováním.
2.	Implementace:
- Rozhraní: Žádné implementace metod.
- Abstraktní třídy: Mohou obsahovat implementace metod.
3.	Dědičnost:
- Rozhraní: Třída může implementovat více rozhraní.
- Abstraktní třídy: Dědičnost: Dědit lze pouze jednu abstraktní třídu.
4.	Případy použití:
- Rozhraní: Pro různorodé třídy, které potřebují společné metody.
- Abstraktní třídy: Pro příbuzné třídy, které sdílejí společnou funkčnost.
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Animal is an abstract base class (ABC). It defines a contract for
    subclasses, ensuring they implement the `make_sound` method.
    """
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


# Demonstrating the use of the interface
if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    print(dog.make_sound())
    print(cat.make_sound())