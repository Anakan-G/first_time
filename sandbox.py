import pygame

import os
os.system("cls")


class Student:
    def __init__(self,first_name,last_name,age,grade_level):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grade_level = grade_level
        self.full_name()

    def full_name(self):
        self.full_name = self.first_name + " " + self.last_name



student01 = Student("John","James",12,7)
print(student01.first_name,student01.last_name,student01.age,student01.grade_level, student01.full_name)


student02 = Student("Jack","Brown",13,8)
print(student02.first_name,student02.last_name,student02.age,student02.grade_level, student02.full_name)

