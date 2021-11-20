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


def partition(mylist):
    a = mylist[:len(mylist)//2]
    b = mylist[len(mylist)//2:]
    print(a, b)


partition([1, 2, 3, 4, 5, 6])


def mergesort(mylist):
    middle = len(mylist) // 2
    list1 = mylist[:(len(mylist) // 2) + 1]


def quicksort(mylist):
    pass


print(bubblesort([1, 5, 8, 2, 89, 43, 123, 5687, 1234, 8, 2, 7, 4, 43, 3, 8]))

print(insertionsort([1, 5, 8, 2, 89, 43, 123,
                     5687, 1234, 8, 2, 7, 4, 43, 3, 8]))
