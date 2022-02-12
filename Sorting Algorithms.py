import time
import random

def bubblesort(mylist):
    finish = False
    while finish == False:
        count = 0
        for i in range(len(mylist)-1):
            if mylist[i] > mylist[i+1]:
                mylist[i], mylist[i+1] = mylist[i+1], mylist[i]
                count += 1
        if count == 0:
            finish = True
    return mylist


def insertionsort(mylist):
    for i in range(1, len(mylist)):
        currentpos = i
        currentval = mylist[i]
        while currentpos > 0 and mylist[currentpos-1] > currentval:
            mylist[currentpos] = mylist[currentpos-1]
            currentpos -= 1
        mylist[currentpos] = currentval
    return mylist

mylist = random.sample(range(1,1000000),1000)
mylist2 = random.sample(range(1,1000000),1000)

start = time.time()
insertionsort(mylist)
end = time.time()
start2=time.time()
bubblesort(mylist2)
end2=time.time()
print(f'(ms) Insertion {(end-start) * 1000} | Bubble {(end2-start2) * 1000}')

# Insertion Sort is consistently faster than bubblesort for all values of n
