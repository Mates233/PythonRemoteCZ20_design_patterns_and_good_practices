class Logger:
    logger_config = ""      # shared class variable
    def __init__(self, file_name="log.txt"):
        self.file_name = file_name

    @staticmethod
    def log(message):
        with open("log.txt", "a") as file:
            file.write(f"{message}\n")

    @classmethod
    def set_logger_config(cls, config):
        cls.logger_config = config


my_logger1 = Logger("my_log1.txt")
my_logger2 = Logger("my_log2.txt")
Logger.logger_config = "new config"     # change the shared class variable

print(my_logger1.logger_config)
print(my_logger2.logger_config)