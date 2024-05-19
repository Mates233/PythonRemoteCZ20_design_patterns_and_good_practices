"""
Iterator
Při používání kolekcí, jako je list nebo set, kromě přidání nebo odebrání položky často chceme provést určité
operace se všemi jejich položkami. Takové kolekce však ukládají data odlišně, aby nedošlo k porušení pravidel SOLID,
neměli bychom uživatelům dávat možnost je přímo upravovat.

Abychom udělili přístup k prvkům kolekce, používáme vzor Iterator, který umožňuje tzv. reiterovat kolem kolekce.
Takový iterátor by měl implementovat metody __iter__() a __next__(), které umožňují postupně procházet prvky kolekce.

1.	Iterabilní kolekce: Definuje kolekci, nad kterou lze iterovat.
2.	Iterátor: Definuje rozhraní pro přístup k prvkům kolekce.
"""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f'Book(title={self.title}, author={self.author})'


class BookCollection:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def __iter__(self):
        return BookIterator(self._books)


class BookIterator:
    def __init__(self, books):
        self._books = books
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._books):
            book = self._books[self._index]
            self._index += 1
            return book
        else:
            raise StopIteration


book1 = Book("The Catcher in the Rye", "J.D. Salinger")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

collection = BookCollection()
collection.add_book(book1)
collection.add_book(book2)
collection.add_book(book3)

for book in collection:
    print(book)
