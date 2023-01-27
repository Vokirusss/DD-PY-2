class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f'Книга "{self.name}". Автор: {self.author}.'

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
        self._pages = pages

    # перегружаем методы __str__ и __repr__ для полноценного представления дочернего класса
    def __str__(self):
        return f"{super().__str__()} Страниц: {self.pages}"  # наследуем и дополняем__str__

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"

    @property
    def pages(self) -> int:
        """ Возвращает количество страниц в бумажной книге """
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """ Установка нового количества страниц в бумажной книге """
        if not isinstance(new_pages, int):
            raise TypeError
        if new_pages <= 0:
            raise ValueError
        self._pages = new_pages


class AudioBook(Book):  # наследуемся от Book
    """ Дочерний класс Аудиокнига """

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError
        if duration <= 0:
            raise ValueError
        self._duration = duration

    def __str__(self):
        return f"{super().__str__()} Продолжительность: {self.duration} минут"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

    @property
    def duration(self) -> float:
        """ Возвращает продолжительность аудиокниги """
        return self._duration

    @duration.setter
    def duration(self, new_duration) -> None:
        """ Установка новой продолжительности аудиокниги """
        if not isinstance(new_duration, float):
            raise TypeError
        if new_duration <= 0:
            raise ValueError
        self._duration = new_duration


if __name__ == '__main__':
    paperBook_sample = PaperBook('1984', 'George Orwell', 314)
    print(paperBook_sample)
    audioBook_sample = AudioBook('1984', 'George Orwell', 634.37)
    print(audioBook_sample)
