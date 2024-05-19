"""
Ukol 5.
Úkol zahrnuje vytvoření meteorologické stanice, která upozorňuje na různé typy zobrazení
(např. aktuální podmínky, statistiky), kdykoli dojde ke změně údajů o počasí.

Co je potřeba udělat:
1.	Třída WeatherData:
- Implementujte metodu register_observer pro přidání pozorovatele do seznamu.
- Implementujte metodu remove_observer pro odstranění pozorovatele ze seznamu.
- Implementujte metodu notify_observers pro volání metody update pro každého pozorovatele
a předejte mu aktuální teplotu, vlhkost a tlak.
2.	Třída CurrentConditionsDisplay:
- Implementujte metodu update pro aktualizaci teploty a vlhkosti.
- Implementujte metodu display pro vypisování aktuálních podmínek.
3.	Třída StatisticsDisplay: Třída StatisticsDisplay:
- Implementujte metodu aktualizace pro aktualizaci maximální, minimální a průměrné teploty.
- Implementujte metodu zobrazení pro tisk statistik teploty.
"""

from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass


class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


# Concrete subject
class WeatherData(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = 0.0
        self._humidity = 0.0
        self._pressure = 0.0

    def register_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
        else:
            print("Observer already exists")

    def remove_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)
        else:
            print("Observer does not exist")

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.measurements_changed()


class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self._temperature = 0.0
        self._humidity = 0.0
        self._weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self.display()

    def display(self):
        print(f"Current conditions: {self._temperature}C degrees and {self._humidity}% humidity")


class StatisticsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self._max_temp = 0.0
        self._min_temp = float('inf')
        self._temp_sum = 0.0
        self._num_readings = 0
        self._weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        # TODO: Update statistics
        pass

    def display(self):
        avg_temp = self._temp_sum / self._num_readings
        print(f"Avg temperature: {avg_temp}, Max temperature: {self._max_temp}, Min temperature: {self._min_temp}")


def main():
    weather_data = WeatherData()

    current_display = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)

    weather_data.set_measurements(21, 65, 30.4)
    weather_data.set_measurements(8, 70, 29.2)
    weather_data.set_measurements(12, 90, 29.2)


if __name__ == "__main__":
    main()
