def getpass(attempt):
    if attempt == 1:
        p = input('Enter the password')
        while len(p) < 6 or len(p) > 8:
            p = input('Error. Password must be between 6 and 8 characters long.')
        return p
    else:
        p2 = input('Enter password again')
        return p2

# main program


attempt = 1
p1 = getpass(attempt)
attempt = 2
p2 = getpass(attempt)
while p1 != p2:
    attempt = 1
    p1 = getpass(attempt)
    attempt = 2
    p2 = getpass(attempt)

print('Password changed successfully')
