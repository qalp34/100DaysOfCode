import json
import re
week_days = ("sunday","monday", "tuesday", "wednesday", "thursday", "friday","saturday")
print(type(week_days))
my_json = json.dumps(week_days)
print(my_json)
print("......")

str = " date is the new oil"
x= re.findall("date", str)
print("serch Result:", x)

print(".....")
print(".....")


python = {
    "languge": "python is an interpreted, high-level, general-purpo",
    "created by": "guido van rossum",
    "date created": "First released in 1991",
}
print (json.dumps(python, indent=4))


