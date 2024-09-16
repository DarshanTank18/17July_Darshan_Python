# What relationship is appropriate for Student and Person?

class Student: 
    def data_1(self): 
        print('I am Student.')

class Student1: 
    def data_2(self): 
        print('I am Student1.')

class Person(Student,Student1): 
    def data_3(self): 
        print('I am Person.')

ps=Person() 
ps.data_1() 
ps.data_2() 
ps.data_3()