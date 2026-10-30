class Book:
    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages

class Ebook(Book):
    # Duplication: Unnecessary and dangerous too
    # Any changes to Book will not be reflected on Ebook
    def __init__(self, title, publisher, pages, format_):
        self.title = title
        self.publisher = publisher
        self.pages = pages
        self.format_ = format_

def main():
    book = Book("Learn Python Programming", "Packt Publishing",
                  500)

    print(book.title)
    print(book.publisher)
    print(book.pages)

    # Normally we would expect Ebook to inherit title, publisher and pages
    # but it doesn't
    try:
        ebook = Ebook(format_="PDF")
        print(ebook.format_)
    except TypeError:
        print("Ebook does not inherit from Book")

if __name__ == "__main__":
    main()