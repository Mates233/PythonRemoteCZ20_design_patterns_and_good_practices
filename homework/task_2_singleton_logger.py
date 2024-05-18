"""
Úkol 2 - Singleton

Pomocí vzoru Singleton vytvořte jednoduchou třídu loggeru, která bude do souboru zapisovat řetězce a datum a čas.
Použijte vnořenou třídu, která shromažďuje funkčnost instance a přetížení __new__ metody."""


import datetime


class Logger:
    _instance = None

    def __new__(cls, file_name="log.txt"):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)     # creation
            cls._instance._initialize(file_name)                # initialization can't be done in __init__
        return cls._instance

    def _initialize(self, file_name):
        self.file_name = file_name

    def _write_log(self, message):
        try:
            with open(self.file_name, 'a') as file:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"{timestamp}: {message}\n")
        except Exception as e:
            print(f"Failed to write log due to: {e}")

    def log(self, message):
        self._write_log(message)


logger1 = Logger("my_log.txt")
logger2 = Logger("ignored.txt")

logger1.log("This is a test log entry.")
logger2.log("This is another log entry.")
