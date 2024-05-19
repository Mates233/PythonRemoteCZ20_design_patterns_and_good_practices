"""
Vzor Memento popisuje, jak spravovat uložené stavy objektu. Představte si hru (např. běžící na konzoli),
která má na určitých místech funkci automatického ukládání. V této hře budete pohybovat svou postavou po celém světě.
 Když k takovému uložení dojde, hra „potřebuje vědět“, např. jaké vybavení má aktuálně vaše postava,
 které úkoly ve hře byly splněny a které probíhají, která místa byla navštívena a která ještě nenavštívena,
 aby se správně zobrazila mapa světa.

Pro implementaci vzoru Memento, potřebujeme:

objekt představující stav aplikace (nebo stav určité části)
objekt představující uložený stav aplikace
schopnost vytvořit uložený objekt z původního stavu
schopnost obnovit původní stav na základě uloženého stavu
objekt, který spravuje uložené stavy

"""
import pickle


class NotSoSimpleClass:
    def __init__(self, name='', count=0):
        self.name = name
        self.count = count

    def get_state(self):
        return pickle.dumps(self.__dict__)

    def restore_state(self, memento):
        self.__dict__.clear()
        self.__dict__.update(pickle.loads(memento))

    def display(self):
        print(f'{self.name} - {self.count}')


sc1 = NotSoSimpleClass('test', 10)
memento = sc1.get_state()
sc2 = NotSoSimpleClass()
sc2.restore_state(memento)
sc2.display()

