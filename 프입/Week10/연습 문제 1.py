class Book:
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages
    def __add__(self, other):
        return self.pages + other.pages

book1 = Book('파이썬', 500)
book2 = Book('자료구조', 600)
print(book1 + book2)