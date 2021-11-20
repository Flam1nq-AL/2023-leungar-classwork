def binarysearch(mylist, item):
    index = -1
    first = 0
    last = len(mylist) - 1
    found = False
    while found == False:
        middle = (first + last) // 2
        print(mylist[middle])
        if mylist[middle] == item:
            found = True
            index = middle
        elif mylist[middle] > item:
            last = middle - 1
        else:
            first = middle + 1
    return middle


def linearsearch(mylist, item):
    found = False
    i = -1
    while found == False:
        i += 1
        if mylist[i] == item:
            found = True
    return i


print(binarysearch([5, 13, 16, 19, 26, 35, 37, 57, 86, 90, 93, 98], 90))

print(linearsearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 2))
