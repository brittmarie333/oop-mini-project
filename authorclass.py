class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography
    
#getters n setters
    def get_name(self):
        return self.__name
    
    def get_favcolor(self):
        return self.__favcolor
    
    def display_details(self):
        return f"Author: {self.__name}, Biography: {self.__biography}"
