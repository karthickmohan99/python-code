class Student:
    clg='xyz'
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
    def display(self):
        print('stu name:',self.name)
        print('stu rollno:',self.rollno)
        print('clg name:',Student.clg)
student1=Student(222,'karthick')
student1.display()
student2=Student(333,'john')
student2.display()
