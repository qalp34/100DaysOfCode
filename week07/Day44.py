class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lanamete = lname

    def printname(self):
            print(self.firstname, self.lastname)
class Student(person):
        def __init__(self, fname, lname):
            super().__init__(self, fname, lname)
x = Student("Mike", "Olsen")
x.printname()


class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lanamete = lname

    def printname(self):
            print(self.firstname, self.lastname)
class Student(person):
        def __init__(self, fname, lname):
            super().__init__(self, fname, lname)
            self.graduationyear =2019
x = Student("Mike", "Olsen")
print(x.graduationyear)


class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lanamete = lname

    def printname(self):
            print(self.firstname, self.lastname)
class Student(person):
        def __init__(self, fname, lname, year):
            super().__init__(self, fname, lname)
            self.graduationyear = year
x = Student("Mike", "Olsen")
print(x.graduationyear)



class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lanamete = lname

    def printname(self):
            print(self.firstname, self.lastname)
class Student(person):
        def __init__(self, fname, lname, year):
            super().__init__(self, fname, lname)
            self.graduationyear = year
        def welcome(self):
            print ("welcome", self.firstname, self.lastname, "to the class of", self.graduationyear) 
x = Student("Mike", "Olsen", 2019)
x.welcome()



