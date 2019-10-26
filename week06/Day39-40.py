
def tri_recursion(k):
    if(k>0):
        result = k+tri_recursion(k-1)
        print(result)
    else:
         result = 0
         return result
         print("\n\nRecursion Example Results")
         tri_recursion(6)

         
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(3)
    print(mydoubler(11))