#Write an algorithm recursively and iteratively that reverses a string

def iterative(alist):
    mylist = []
    for i in range(len(alist)):
        mylist.append(alist[len(alist)-(i+1)])
    return mylist

def recursive(alist):
    if len(alist) == 0:
        return []                                                                                                                                                                                   
    else:
        return [alist[-1]] + recursive(alist[:-1])
    
x = recursive(['a','b','c'])
print(x)


        
        