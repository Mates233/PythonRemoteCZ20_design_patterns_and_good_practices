"""
Úkol 2 - Singleton

Pomocí vzoru Singleton vytvořte jednoduchou třídu loggeru, která bude do souboru zapisovat řetězce a datum a čas.
Použijte vnořenou třídu, která shromažďuje funkčnost instance a přetížení __new__ metody."""


class Logger:
    class __Logger:
        def __init__(self, file_name):
            self.file_name = file_name

        def _write_log(self, message):
            """Helper method to write a log message to a file with a timestamp."""
            pass

        def log(self, message):
            """Public method to write a log."""
            pass
