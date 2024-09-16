# What relationship is appropriate for Course and Faculty?
class Student: 
    def data_1(self): 
        print('I am Student and i am learning Python.')

class Teacher: 
    def data_2(self): 
        print('My teacher is sanket sir.')

class Person(Student,Teacher): 
    def data_3(self): 
        print('My name is Darshan.')

ps=Person() 
ps.data_1() 
ps.data_2() 
ps.data_3()