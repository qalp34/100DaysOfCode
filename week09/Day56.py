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
print(json(x,indent=4))


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
print(json.dumps(x,indent=4, separators=(".", "=")))


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
print(json.dumps(x,indent=4, sort_keys=True))





