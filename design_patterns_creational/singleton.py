class ConfigSingleton:
    _instance = None

    def __init__(self):
        self.value = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigSingleton, cls).__new__(cls)
            # Initialize any attributes of the singleton here, if necessary
            cls._instance.value = "Default Configuration"
        return cls._instance

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

# Usage
config1 = ConfigSingleton()
config2 = ConfigSingleton()

#print(config1 == config2)

config1.set_value("New Configuration")
#print(config2.get_value())


class TestNew:
    def __new__(cls, *args, **kwargs):
        print("Creating instance")
        return super(TestNew, cls).__new__(cls)

    def __init__(self):
        self.value = None
        print("Initializing instance")

print(TestNew())
