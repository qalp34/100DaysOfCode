class MyClass:
    x = 5
    print(MyClass)



class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = person("John", 36)
print(p1.name)
print(p1.age)


class person:
    def __init__(mySillyObject, name, age):
       mysillyobject.name = name
       mysillyobject.age = age
    def myfunc(abc):
        print("hello my name is " + abc.name)
p1 = person("John", 36)
p1.myfunc()




