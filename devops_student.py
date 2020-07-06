# imports parent class student_data
from student_data import *


class Devops(Student):
    def __init__(self, age, course):
        super().__init__(age)
        self.__course = course

    def set_course(self, value):
        self.__course = value

    def get_course(self):
        return self.__course

# instances
marcus = Devops(23, 'SQL, Python')
jim = Devops(25, 'SQL')
bob = Devops(30, 'SQL, Python, AWS')

marcus.set_age(28)
# ford.__age = 23 # uncommenting this will produce an error because age has been set to a private variable
print(marcus.get_age())
# ford.__course # will also produce an error
print(marcus.get_course())

