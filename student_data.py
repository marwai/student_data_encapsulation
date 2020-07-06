class Student:
    def __init__(self, age):
        # __speed and __color has been to set to private to prevent accidentally changing the variable
        self.__age = age


    # set attribute (set attr) has to be called to change the speed
    def set_age(self, value):
        self.__speed = value

    def get_age(self):
        return self.__speed



