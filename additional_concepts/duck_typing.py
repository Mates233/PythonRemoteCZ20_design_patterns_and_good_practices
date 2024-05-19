"""
Duck typing je koncept v programování, kdy se vhodnost objektu určuje spíše podle přítomnosti určitých metod
a vlastností než podle skutečného typu objektu. Název pochází z věty: „Pokud to vypadá jako kachna, plave to
jako kachna a kváká to jako kachna, pak to pravděpodobně je kachna.“.

Klíčové body:

1.Chování nad typem: V duck typingu je chování objektu (tj. metody a vlastnosti, které má)
důležitější než třída nebo typ objektu.
2.Flexibilita: V případě, že se jedná o typ chování, je možné, že se jedná o typ chování:
To umožňuje flexibilnější a dynamičtější kód, protože lze použít libovolný objekt,
který implementuje požadované chování, bez ohledu na hierarchii dědičnosti.
3.Polymorfismus: Duck typing podporuje polymorfismus, což umožňuje, aby funkce nebo metody pracovaly
s objekty různých typů, pokud implementují očekávané chování.
4.Žádné explicitní smlouvy: Na rozdíl od jazyků, které k vynucení implementace metod používají
rozhraní nebo abstraktní základní třídy, kachní typování spoléhá na přítomnost metod a vlastností za běhu.


Zatímco duck typování poskytuje flexibilitu, některé návrhové vzory využívají nebo vyžadují vynucení
přítomnosti metod a struktury poskytované abstraktními bázovými třídami nebo rozhraními. Patří mezi ně vzory, kde:
-konzistence a zaměnitelnost komponent jsou klíčové (Decorator, Strategy, Factory Method).
-Formální smlouva pro metody je nezbytná k zajištění správné implementace (Interpreter, Template Method).
-Struktura a přehlednost jsou důležité pro zachování robustnosti a omezení chyb za běhu.

V těchto případech formalismus poskytovaný abstraktními základními třídami nebo rozhraními pomáhá zajistit,
aby se systém choval podle očekávání a aby všechny komponenty dodržovaly definované smlouvy,
což vede k udržovatelnějšímu a spolehlivějšímu kódu.
"""


class Dog:
    def make_sound(self):
        return "Woof!"


class Cat:
    def make_sound(self):
        return "Meow!"


class Person:
    def make_sound(self):
        return "I'm quacking like a duck!"


def in_the_forest(animal):
    """
    This function demonstrates duck typing. It accepts any object that has a
    make_sound method, regardless of the object's actual type.
    """
    print(animal.make_sound())


if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    person = Person()

    in_the_forest(dog)
    in_the_forest(cat)
    in_the_forest(person)
