age = 36
txt = "My name is John, I am " + age
print(txt)

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


quantity = 3
itemno = 567
price = 49.99
myorder = "I want {} pieces of item {} for {} dollers."
print(myorder.format(quantity,itemno,price))

quantity = 3
itemno = 567
price = 49.99
myorder = "I want to pay {2} dollers for {0} pieces of item {1}."
print(myorder.format(quantity,itemno,price))