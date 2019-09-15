thisdict =     {
    "brand": "ford",
    "model": "mustang",
    "year": 1964 
}
if "model" in thisdict:
    print("yes, 'model' is one of the keys in the thisdict dictionary")



thisdict =     {
    "brand": "ford",
    "model": "mustang",
    "year": 1964 
}
print(len(thisdict))

    

thisdict =     {
    "brand": "ford",
    "model": "mustang",
    "year": 1964 
}
thisdict["color"] = "red"
print(thisdict)


thisdict =     {
    "brand": "ford",
    "model": "mustang",
    "year": 1964 
}
thisdict.pop("model")
print(thisdict)


thisdict =     {
    "brand": "ford",
    "model": "mustang",
    "year": 1964 
}
thisdict.popitem()
print(thisdict)


thisdict =     {
    "brand": "ford",
    "model": "mustang",
    "year": 1964 
}
del thisdict
print(thisdict) # this will cause error because "this list" no longer exits


thisdict =     {
    "brand": "ford",
    "model": "mustang",
    "year": 1964 
}
thisdict.clear()
print(thisdict)


