class Book:
    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages

class Ebook(Book):
    # If we change the name of class Book to sth else, it will be reflected
    def __init__(self, title, publisher, pages, format_):
        super().__init__(title, publisher, pages)
        # It is also done in another way
        # super(Ebook, self).__init__(title, publisher, pages)
        self.format_ = format_

def main():
    ebook = Ebook("Learn Python Programming", "Packt Publishing",
                  500, "PDF")

    print(ebook.title)
    print(ebook.publisher)
    print(ebook.pages)
    print(ebook.format_)

if __name__ == "__main__":
    main()