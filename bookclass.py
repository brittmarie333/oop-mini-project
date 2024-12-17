class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__availability = True 
    
#getters n setters
    def get_title(self):
        return self.__title
    
    def set_title(self, title):
        self.__title = title
    
    def get_author(self):
        return self.__author
    
    def set_author(self, author):
        self.__author = author
    
    def get_availability(self):
        return self.__availability
    
    def set_availability(self, status):
        self.__availability = status
    
    def display_details(self):
        return f"Title: {self.__title}, Author: {self.__author}, Genre: {self.__genre}, Published: {self.__publication_date}, Available: {'Yes' if self.__availability else 'No'}"
