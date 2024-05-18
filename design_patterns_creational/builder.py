class Car:
    def __init__(self):
        self.seats = None
        self.engine = None
        self.trip_computer = False
        self.gps = False

    def __str__(self):
        return f"Car with {self.seats} seats, engine type: {self.engine}, " \
               f"trip computer: {'yes' if self.trip_computer else 'no'}, GPS: {'yes' if self.gps else 'no'}"


class CarBuilder:
    def __init__(self):
        # better implementation in this case is to start with
        self.car = None

    def add_seats(self, number):
        self.car.seats = number
        return self

    def add_engine(self, engine_type):
        self.car.engine = engine_type
        return self

    def add_trip_computer(self):
        self.car.trip_computer = True
        return self

    def add_gps(self):
        self.car.gps = True
        return self

    def build(self):
        built_car = self.car
        self.car = None
        return built_car


builder = CarBuilder()

sport_car = builder.add_seats(2).add_engine('V8').add_trip_computer().build()
print(sport_car)
suv_car = builder.add_seats(5).add_engine('V6').add_trip_computer().add_gps().build()
print(suv_car)
