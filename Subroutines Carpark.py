carpark = [['empty' for a in range(6)] for b in range(10)]


def emptycarpark():
    return [['empty' for a in range(6)] for b in range(10)]


def parkcar(carpark):
    row = int(input('What row do you want to park in?'))
    column = int(input('What column do you want to park in?'))
    reg = str(input('What is the registration number?'))
    carpark[row-1][column-1] = reg


def removecar(carpark):
    row = int(input('What row do you want to remove the car??'))
    column = int(input('What column do you want to remove the car?'))
    carpark[row-1][column-1] = 'empty'


def display(carpark):
    for r in carpark:
        for c in r:
            print(c, end=" ")
        print()


print('Option 1: Set all spaces in car park to empty')
print('Option 2: Park a Car')
print('Option 3: Remove a Car')
print('Option 4: Display Car park')
print('Option 5: Quit')
option = int(input('Please enter your option'))
while option < 1 or option > 5:
    option = int(input('That is not a valid option 1-5. Please try again'))


while option != 5:
    if option == 1:
        carpark = emptycarpark()
    elif option == 2:
        parkcar(carpark)
    elif option == 3:
        removecar(carpark)
    elif option == 4:
        display(carpark)
    else:
        option = int(input('That is not a valid option 1-5. Please try again'))

    print('Option 1: Set all spaces in car park to empty')
    print('Option 2: Park a Car')
    print('Option 3: Remove a Car')
    print('Option 4: Display Car park')
    print('Option 5: Quit')
    option = int(input('Please enter your option'))

print('Goodbye')
