list1 = [2, 5, 15, 36, 47, 56, 59, 78, 156, 244, 268]
list2 = [18, 39, 42, 43, 66, 69, 100]

for i in range(len(list2)):
    for x in range(0, len(list1)-1):
        if list2[i] > list1[x] and list2[i] < list1[x+1]:
            list1.insert(x+1, list2[i])

print(list1)
