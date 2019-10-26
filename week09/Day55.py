import json
# some json:
x = '{ "name":, "age":30, "city":"new york"}'
y = json.loads(x)
print(y["age"])


x = {
    "name": "john",
    "age":30,
    "city": "new york" 
}
y = json.dumps(x)
print(y)

print(json.dumps({"name": "john", "age": 30}))
print(json.dumps(["apple", "banana"]))
print(json.dumps(("apple", "banana")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

import json

x = {
    "name": "john",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann" , "Billy"),
    "pets": None,
    "cars": [
        {"model": "Bmw 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg":24.1}
    ]
}
y = json.dumps(x)
print(y)






