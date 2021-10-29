class Person:
    def __init__(self,name):
        self.name=name
    def speak(self,msg='(calling the base class)'):
         print(self.name,msg)
class Man(Person):
    def speak (self,msg='It\'s a beautiful evening'):
        print(self.name,':\n\tHello!',msg)
class Hombre(Person):
    def speak(self,msg='Es una tardohermosa'):
        print(self.name,':\n\tHello!',msg)
guy1=Man('Richard')
guy1.speak()
guy2=Hombre('Ricardo')
guy2.speak()
Person.speak(guy1)
Person.speak(guy2)
