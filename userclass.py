class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []
    
#getters n setters
    def get_name(self):
        return self.__name
    
    def get_library_id(self):
        return self.__library_id
    
    def borrow_book(self, book):
        self.__borrowed_books.append(book)
        book.set_availability(False)
    
    def return_book(self, book):
        self.__borrowed_books.remove(book)
        book.set_availability(True)
    
    def display_details(self):
        borrowed_titles = [book.get_title() for book in self.__borrowed_books]
        return f"Name: {self.__name}, Library ID: {self.__library_id}, Borrowed Books: {', '.join(borrowed_titles) if borrowed_titles else 'None'}"
