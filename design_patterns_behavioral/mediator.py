"""
Vzor Mediator je podobný vzoru Observer v tom, že popisuje, jak provést a zpracovat požadavek.
Tento vzor se vyplatí použít, když v aplikaci najdeme mnoho komponent, které spolu nějak komunikují.
Když se vztahy mezi nimi zkomplikují,

Mediátor je další objekt vložený mezi všechny tyto komponenty, které místo toho, aby spolu přímo komunikovaly,
komunikují pouze s ním.
"""

from abc import ABC, abstractmethod


class ChatRoomMediator(ABC):
    @abstractmethod
    def show_message(self, user, message):
        pass


class ChatRoom(ChatRoomMediator):
    def show_message(self, user, message):
        print(f"[{user.get_name()}]: {message}")


class User:
    def __init__(self, name, chat_room):
        self._name = name
        self._chat_room = chat_room

    def get_name(self):
        return self._name

    def send_message(self, message):
        self._chat_room.show_message(self, message)


chat_room = ChatRoom()

user1 = User("Alice", chat_room)
user2 = User("Bob", chat_room)

user1.send_message("Hello, Bob!")
user2.send_message("Hi, Alice!")