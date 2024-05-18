"""
Předpokládejme, že aplikace, na které pracujeme, je nainstalována přímo na serveru klienta.
Po nějaké době nás klient informuje, že aplikace časem přestane fungovat z důvodu nedostatečné dostupné paměti RAM.
Po analýze problému se ukáže, že v paměti je mnoho (velmi mnoho) objektů stejného typu.

Design
Abychom vyřešili výše popsaný problém, abychom omezili paměť aplikace, můžeme použít strukturní vzor Flyweight.
Máme-li velký počet objektů stejného typu, můžeme se pokusit izolovat společnou část (nebo několik) těchto objektů.

Poté upravíme každý z původních objektů následovně:

namísto samostatné kopie „společných“ polí obsahuje odkaz na objekt, který tuto společnou část představuje.
"""


class Flyweight:
    _shared_state = ""

    def __init__(self, private_state):
        self._private_state = private_state


f1 = Flyweight("this is private")
Flyweight._shared_state = "is this private?"
print(f1._shared_state)
f2 = Flyweight("this is also private")
Flyweight._shared_state = "no it is not"

print(f1._shared_state)
print(f2._shared_state)
print(f1._private_state)
print(f2._private_state)