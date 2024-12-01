from typing import Self


class Book:
    def __init__(self, title: str, pages: int) -> None:
        self.title = title
        self.pages = pages

    def __len__(self) -> int:
        return self.pages

    def __add__(self, other: Self) -> Self:
        combined_title = f"{self.title} & {other.title}"
        combined_pages = self.pages + other.pages
        return Book(combined_title, combined_pages)


def main() -> None:
    book_1: Book = Book("Book_1", 100)
    book_2: Book = Book("Book_2", 200)
    print(len(book_1))
    print(len(book_2))
    print(book_1.__len__())
    print(book_2.__len__())

    combined_books: Book = book_1 + book_2
    print(combined_books.title)
    print(combined_books.pages)
    ...


if __name__ == '__main__':
    main()
