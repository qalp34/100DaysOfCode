thisset = {1, 3, 5, 7, 8}
print(thisset)


thisset = {1, 3, 5, 7, 8}
thisset.update([4, 8, 12])
print(thisset)


thisset = {1, 3, 5, 7, 8}
thisset.remove(8)
print(thisset)


thisset = {1, 3, 5, 7, 8}
del thisset
print(thisset)



thisdict = {
    "name" : "pigeon",
   " type" : "bird",
   "skin cover" : "feathers"
}
print(thisdict)



thisdict = {
    "name" : "pigeon",
   "type" : "bird",
   "skin cover" : "feathers"
}
x = thisdict["type"]
print(x)



thisdict = {
    "name" : "pigeon",
    "type" : "bird",
   "skin cover" : "feathers"
}
x = thisdict.get("type")
print(x)



thisdict = {
    "name" : "pigeon",
   "type" : "bird",
   "skin cover" : "feathers"
}
thisdict["skin cover"] = "leather" 
print(thisdict)
