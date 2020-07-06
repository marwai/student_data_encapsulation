# imports parent class student_data
from student_data import *


class Devops(Student):
    def __init__(self, age, course):
        super().__init__(age)
        self.__course = course

    # Encapsulation prevents accidentally changing an object's variable. Prevents other classes from accessing methods
    # within classes that are protected
    def set_course(self, value):
        self.course = value

    def get_course(self):
        return self.__course

# instances
dev = Devops(23, 'SQL, Python')
stu = Student(23)

# 1) setattr method
# dev.set_age(28)
# dev.__age = 23 # uncommenting this will produce an error because age has been set to a private variable
# print(dev.get_age())

# 2) second example
# marcus.__course # will also produce an error
# print(marcus.get_course())
# accessible through name_mangling

# 3) Privitising attribute
# dev._Student__set_age(35)
# print(dev.get_age())
