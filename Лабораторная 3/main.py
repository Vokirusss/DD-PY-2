class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:  # запрещаем изменять name и author
        return self._name

    @property
    def author(self) -> str:
        return self._author


class PaperBook(Book):  # наследуемся от Book
    """ Дочерний класс Бумажная книга  """

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)  # вызываем конструктор родительского класса для его расширения
        if not isinstance(pages, int):
            raise TypeError
        if pages <= 0:
            raise ValueError
        self.pages = pages

    # перегружаем методы __str__ и __repr__ для полноценного представления дочернего класса
    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Страниц: {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):  # наследуемся от Book
    """ Дочерний класс Аудиокнига """

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError
        if duration <= 0:
            raise ValueError
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность: {self.duration} минут"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"


if __name__ == '__main__':
    paperBook_sample = PaperBook('1984', 'George Orwell', 314)
    audioBook_sample = AudioBook('1984', 'George Orwell', 634.37)

    print(paperBook_sample)
    # paperBook_sample.name = "Brave New World" # проверка на возможность перезаписи
    print(audioBook_sample)
    # audioBook_sample.name = "Brave New World"  # проверка на возможность перезаписи
