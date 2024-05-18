"""
Účel: Poskytuje rozhraní, které zjednodušuje provádění operace nebo integruje více rozhraní do jednoho

Vlastnosti:

implementační metody obvykle složené z volání závislostí
málo / mnoho závislostí v konstruktoru
zjednodušení operace
"""


class Light:
    def on(self):
        print("The light is on")

    def off(self):
        print("The light is off")


class Thermostat:
    def set_temperature(self, temperature):
        print(f"Setting temperature to {temperature} degrees")


class SecuritySystem:
    def arm(self):
        print("The security system is armed")

    def disarm(self):
        print("The security system is disarmed")


class HomeAutomationFacade:
    def __init__(self):
        self.light = Light()
        self.thermostat = Thermostat()
        self.security_system = SecuritySystem()

    def leave_home(self):
        print("Leaving home...")
        self.light.off()
        self.thermostat.set_temperature(18)
        self.security_system.arm()

    def arrive_home(self):
        print("Arriving home...")
        self.light.on()
        self.thermostat.set_temperature(22)
        self.security_system.disarm()


def main():
    home_automation = HomeAutomationFacade()

    # User leaves home
    home_automation.leave_home()

    print("\n")

    # User arrives home
    home_automation.arrive_home()


if __name__ == '__main__':
    main()
