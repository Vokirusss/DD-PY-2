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
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id}, name={self.name!r}, pages={self.pages})'


class Library:

    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books

    def __str__(self) -> str:
        return str(self.books)

    def __repr__(self):
        return f'Library(books={self.books})'

    def get_next_book_id(self) -> int:  # сюда попадает список с объектами Book. Why?
        if self.books:
            next_book_id = len(self.books) + 1  # заведомо неверный подход, но пусть пока хотя бы так
        else:
            next_book_id = 1
        return next_book_id

    def get_index_by_book_id(self, id_):
        for book_item in self.books:
            for attr_ in vars(book_item):
                print(attr_)
            # for i in self.books[i]:
            #     if id_ in self.books[i]:
            #         print(id_)
            #         return [index for index, book in enumerate(self.books)]
            #     else:
            #         raise ValueError("ID is not found.")


if __name__ == '__main__':
    lib1 = Library()
    print('Empty instance:', lib1)

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    lib2 = Library(books=list_books)
    print('Filled instance:', lib2)

    print('ID for filled instance:', lib2.get_next_book_id())
    print(lib2.get_index_by_book_id(1))

    # empty_library = Library()  # инициализируем пустую библиотеку
    # print('id для пустой библиотеки: ', empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки
    #
    # list_books = [
    #     Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    # ]
    # library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    # print('id для НЕпустой библиотеки: ', library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки
    #
    # print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1

#     def __iter__(self):
#         return LibraryIter(self)


# class LibraryIter:
#
#     def __init__(self, book):
#         self._id_ = book.id_
#         self._name = book.name
#         self._pages = book.pages
#         self.book_lib_size = len(self)
#         self.current_index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current_index < self.book_lib_size:
#             self.current_index += 1
#             return "It works"
#         raise StopIteration
