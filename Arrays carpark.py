carpark = [['empty' for a in range(10)] for b in range(10)]

again = True

while again == True:
    row = int(input('What row do you want to park in?'))
    while row < 1 or row > 10:
        row = int(input('That is not a valid row 1-10. Please try again.'))
    column = int(input('What column do you want to park in?'))
    while column < 1 or column > 10:
        column = int(
            input('That is not a valid column 1-10. Please try again.'))
    reg = str(input('What is the registration number?'))
    if carpark[row-1][column-1] == 'empty':
        carpark[row-1][column-1] = reg
        again = False
    else:
        print('That space is taken. please re enter the grid references.')
        again = True

for r in carpark:
    for c in r:
        print(c, end=" ")
    print()
