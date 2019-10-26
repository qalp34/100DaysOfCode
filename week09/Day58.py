import re
str = "The rain in spain" 
x = re.findall("ai", str)
print(x)

import re
str = "The rain in spain" 
x = re.search("\s", str)
print("the first white-space character is located in position", x.start() )


import re
str = "The rain in spain" 
x = re.search("portugal", str)
print(x)


import re
str = "The rain in spain" 
x = re.split("\s", str)
print(x)



