BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:

    def __init__(self, id_: int, name: str, pages: int):
        """
        Конструктор объекта класса Book

        :param id_: идентификатор книги, int
        :param name: название книги, str
        :param pages: количество страниц в книге, int

        """
        if not isinstance(id_, int):
            raise TypeError
        if id_ <= 0:
            raise ValueError
        self.id = id_

        self.name = name

        if not isinstance(pages, int):
            raise TypeError
        if pages <= 0:
            raise ValueError
        self.pages = pages

    def __str__(self) -> str:
        return f'{self.id} Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id}, name={self.name!r}, pages={self.pages})'


class Library:

    def __init__(self, books=None):
        """
        Конструктор объекта класса Library

        :param books: список книг, по умолчанию пустой

        """
        if books is None:
            books = []
        self.books = books

    def __str__(self) -> str:
        return str(self.books)

    def __repr__(self):
        return f'Library(books={self.books})'

    def get_next_book_id(self) -> int:
        """ Создание id новой книги для добавления в библиотеку """
        if self.books:
            return self.books[-1].id + 1
        else:
            return 1

    def get_index_by_book_id(self, id_: int) -> int:
        """
        Метод возвращает индекс книги в списке по её id

        :param id_: id, указанный пользователем
        :raise ValueError: вызывается ошибка, если книги с запрашиваемым id нет в списке

        """
        for index, instance in enumerate(self.books):
            if id_ == instance.id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
