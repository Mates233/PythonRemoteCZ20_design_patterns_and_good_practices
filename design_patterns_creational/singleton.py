class ConfigSingleton:
    # Všimněte si, že potřebujeme proměnnou na úrovni třídy, a ne proměnnou instance.
    # Více o class variables vs instance variables zde:
    # https://medium.com/@pouyahallaj/class-vs-instance-variables-in-python-5573e71c99b5
    _instance = None

    def __init__(self):
        self.value = None

    def __new__(cls):
        if cls._instance is None:
            # Řádek 14 vytvoří objekt naší třídy, rozdíl medzi new a init:
            # https://builtin.com/data-science/new-python
            cls._instance = super(ConfigSingleton, cls).__new__(cls)
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
