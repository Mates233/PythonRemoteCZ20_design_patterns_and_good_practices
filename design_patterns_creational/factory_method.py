from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass


class Truck(Transport):
    def deliver(self):
        return "Deliver by land in a box."


class Ship(Transport):
    def deliver(self):
        return "Deliver by sea in a container."


class Plane(Transport):
    def deliver(self):
        return "Deliver by air in a container."


class Logistics(ABC):
    @abstractmethod
    def create_transport(self):
        pass

    def plan_delivery(self):
        # The factory method is called here to create a transport object.
        transport = self.create_transport()
        return transport.deliver()


class RoadLogistics(Logistics):
    def create_transport(self):
        return Truck()


class SeaLogistics(Logistics):
    def create_transport(self):
        return Ship()


class AirLogistics(Logistics):
    def create_transport(self):
        return Plane()


road_logistics = RoadLogistics()
print(road_logistics.plan_delivery())

sea_logistics = SeaLogistics()
print(sea_logistics.plan_delivery())

air_logistics = AirLogistics()
print(air_logistics.plan_delivery())