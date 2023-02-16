class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def say_hello(self):
        print(f"Hello, my name is {self.name} and my age is {self.age}")
#creating my object
person1=Person("Johannes", 30)
person1.say_hello()
person2=Person("Henry",64)
person2.say_hello()
person3=Person("Erica",28)
person3.say_hello()
person4=Person("George",43)
person4.say_hello()
#Create a class called cars with the following attributes/properties
#make.mode.year then create a function that prints make,model and year

class Cars:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def say_this(self):
        print(f"Hello,this is {self.make} and the model is {self.model} made in the year {self.year}")
car1=Cars("Toyota","Belta", 2012)
car1.say_this()
car2=Cars("Mercedes Benz","S500", 2009)
car2.say_this()
car3=Cars("Chevrolet","Trailblazer",2016)
car3.say_this()
car4=Cars("Mitsubishi","Lancer",2007)
car4.say_this()
#Inheritance

class Ballers:
    def __init__(self,name,age,country):
        self.name=name
        self.age=age
        self.country=country
    def say_this(self):
        print(f"Hi ,my name is {self.name}, I suam {self.age}.I come from {self.country} ")
baller1=Ballers("Jude Bellingham",20, "England")
baller1.say_this()
baller2=Ballers("Lionel Messi",34, "Argentina")
baller2.say_this()
















