class Book:
    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages

class Ebook(Book):
    def __init__(self, title, publisher, pages, format_):
        Book.__init__(self, title, publisher, pages)
        self.format_ = format_

def main():
    ebook = Ebook("Learn Python Programming", "Packt Publishing", 500, "PDF")
    print(ebook.title)
    print(ebook.publisher)
    print(ebook.pages)
    print(ebook.format_)

    book = Book("Learn C", "Manning", 300)
    print(book.title)
    print(book.publisher)
    print(book.pages)

    book.format_ = "ebup"
    print(book.format_)

if __name__ == "__main__":
    main()