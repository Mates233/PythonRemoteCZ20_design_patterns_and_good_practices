"""
Ve složitých aplikacích obvykle existuje určitá konfigurace. Tato konfigurace ovlivňuje referenční hodnoty v objektech
 a specifické hodnoty atributů takových objektů mohou ovlivnit chování aplikace během provádění určitého procesu.
 Výše uvedený popis stručně představuje chování vzoru State. Popisuje, jak objekt mění své chování jako
 odpověď na určitý (stejný) požadavek v závislosti na jeho stavu.

Design a příklad
Vymodelujeme semafor, který může být ve třech různých stavech: Zelená, žlutá a červená.
"""

from abc import ABC, abstractmethod


class TrafficLightState(ABC):
    @abstractmethod
    def handle(self, traffic_light):
        pass


class GreenState(TrafficLightState):
    def handle(self, traffic_light):
        print("Green -> Yellow")
        traffic_light.state = YellowState()


class YellowState(TrafficLightState):
    def handle(self, traffic_light):
        print("Yellow -> Red")
        traffic_light.state = RedState()


class RedState(TrafficLightState):
    def handle(self, traffic_light):
        print("Red -> Green")
        traffic_light.state = GreenState()


class TrafficLight:
    def __init__(self):
        self.state = GreenState()  # zakladni stav

    def change(self):
        self.state.handle(self)


if __name__ == "__main__":
    traffic_light = TrafficLight()

    for _ in range(6):  # Simulujeme změnu stavu světelného signálu
        traffic_light.change()