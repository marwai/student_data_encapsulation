
class Student:
    def __init__(self, age):
        # __speed and __color has been to set to private to prevent accidentally changing the variable
        self.__age = age


    # set attribute (set attr) has to be called to change the age
    # def set_age(self, value):
    #     self.__age = value

    def __set_age(self, value):
        self.__age = value

    def get_age(self):
        return self.__age
