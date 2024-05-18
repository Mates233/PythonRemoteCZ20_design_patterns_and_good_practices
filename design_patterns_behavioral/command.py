"""
Účelem vzoru chování Command je oddělit objekty, které odesílají požadavky, od objektů, které přijímají jejich výsledky.
Umožňuje to zavedením objektu představujícího příkaz, který takový proces provádí.
Volitelně může být příkaz také schopen vrátit zpět výsledek takového procesu.

Zabalením provádění procesu do samostatného objektu zachováme pravidla SOLID odstraněním potenciální silné vazby
mezi odesílatelem a příjemcem výsledku požadavku.

Design a příklad
Hlavním prvkem, který musíme vytvořit, je společný objekt představující provádění procesu.
Volitelně může být možné zrušit provedení příkazu.

Objekty potřebné k provedení příkazu nejčastěji získává v konstruktoru implementace.

1. Command Interface: Deklaruje rozhraní pro provedení operace.
2. Concrete Command: Implementuje rozhraní příkazu a definuje vazbu mezi přijímačem a akcí.
3. Receiver: Příkaz, který je určen k provedení příkazu: Příkaz: Ví, jak provést operace spojené s provedením požadavku.
4. Invoker: Vyvolávač: Vyvolává příkaz: Žádá příkaz o provedení požadavku.
5. Client: Vyplní příkaz k provedení příkazu: Vytvoří objekt ConcreteCommand a nastaví jeho příjemce.
"""


from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class WriteCommand(Command):
    def __init__(self, receiver, text):
        self.receiver = receiver
        self.text = text

    def execute(self):
        self.receiver.write(self.text)

    def undo(self):
        self.receiver.undo()


class TextEditor:
    def __init__(self):
        self.text = ""
        self.history = []

    def write(self, text):
        self.history.append(self.text)
        self.text += text
        print(f"Current Text: {self.text}")

    def undo(self):
        if self.history:
            self.text = self.history.pop()
        print(f"Undo Text: {self.text}")

    def redo(self, text):
        self.history.append(self.text)
        self.text += text
        print(f"Redo Text: {self.text}")


class TextEditorInvoker:
    def __init__(self):
        self.commands = []
        self.undo_commands = []

    def execute_command(self, command):
        command.execute()
        self.commands.append(command)
        self.undo_commands.clear()

    def undo(self):
        if self.commands:
            command = self.commands.pop()
            command.undo()
            self.undo_commands.append(command)

    def redo(self):
        if self.undo_commands:
            command = self.undo_commands.pop()
            command.execute()
            self.commands.append(command)


def main():
    editor = TextEditor()
    invoker = TextEditorInvoker()

    # Write text
    command1 = WriteCommand(editor, "Hello, ")
    invoker.execute_command(command1)

    command2 = WriteCommand(editor, "World!")
    invoker.execute_command(command2)

    # Undo the last command
    invoker.undo()

    # Redo the last undone command
    invoker.redo()

if __name__ == "__main__":
    main()