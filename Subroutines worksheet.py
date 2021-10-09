def multiples(start_num, end_num, pupilName, table):
    print('Hi ' + pupilName + ', here is your times table:')
    for i in range(start_num, end_num + 1):
        total = table * i
        print('{}  x  {}  =  {}'.format(table, i, total))


# Main Program


pupilName = input('What is your name?')
table = int(input('What times table would you like to see?'))
start_num = int(input('Enter the starting number'))
end_num = int(input('Enter the end number'))
multiples(start_num, end_num, pupilName, table)
