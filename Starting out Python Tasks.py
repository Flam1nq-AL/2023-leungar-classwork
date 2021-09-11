def names():
    first = str(input("Please enter your first name"))
    second = str(input("Please enter your second name"))
    return first + " " + second

def password():
    password = input("Please enter your password")
    while len(password) > 6:
        password = input("Please enter your password again, it is too long.")

def options():
    num = input("Please enter a number between 1-3.")
    while num != "1" and num != "2" and num != "3":
        num = input("Please re-enter the number between 1-3 as your input is invalid.")
    print("You have selected option " + num)

def division():
    num = int(input("Please enter the number"))
    div = int(input("Please enter the divisor"))
    num2 = num // div
    rem = num % div
    return num2 + " remainder " rem

def splitting():
    num = input("Please enter a 3 digit number.")
    print(num[0] + " hundreds, " + num[1] + " tens, and " + num[2] + " units.")

def numseq():
    for i in range(10):
        print(i )
        

def timestables():
    num = int(input("Please enter the number"))
    for i in range(10):
        print(num*i)

def comparison2():
    num = int(input("Enter the first number"))
    num2 = int(input("Enter the second number"))
    if num > num2:
        print(num,num2)
    else:
        print(num2,num)

def comparison3():
    num = int(input("Enter the first number"))
    num2 = int(input("Enter the second number"))
    num3 = int(input("Enter the third number"))
    if num > num2 and num> num3:
        if num2 > num3:
            print(num,num2,num3)
        else:
            print(num,num3,num2)
    if num2 > num and num2> num3:
        if num > num3:
            print(num2,num,num3)
        else:
            print(num2,num3,num)
    else:
        if num > num2:
            print(num3,num,num2)
        else:
            print(num3,num2,num)

def words():
    sentence = str(input("Please enter the sentence"))
    words = sentence.split(" ")
    return len(words)

def seconds():
    time = input("Please enter the time")
    times = time.split(":")
    times = [int(i) for i in times]
    total = (times[0] * 3600) + (times[1] * 60) + times[2]
    print(total)

def factors():
    factors = []
    num = int(input("Please enter the number"))
    for i in range(len(num)):
        if num % i == 0:
            factor.append(i)
    print(factors)

def caesar():
    word = str(input("Please enter the word"))
    word = word.lower()
    word = word.split("")
    for i in range(len(word)):
        word[i] = ord(word[i]) + 9
    word = word.join("")
    print(word)


def reversed():
    word = str(input("Please enter the word"))
    if word[::-1] == word:
        print("This word is a palindrome!")
    else:
        return word[::-1]

def rps():
    moves = ["r", "p", "s"]
    ai_move = moves[randint(0,2)]
    move = input("rock paper or scissors? enter R P or S")
    move = move.lower()
    while move != "r" or move !="s" or move != "p":
        move = input("Please enter r p or s")
    
    if move == ai_move:
        print("tie!")
    
    if move == "r":
        if ai_move == "p":
            print("You lose! paper Beats rock!")
        else:
            print("you win!")
    
    if move == "s":
        if ai_move == "r":
            print("You lose! rock Beats scissors!")
        else:
            print("you win!")
    
    if move == "p":
        if ai_move == "s":
            print("You lose! paper Beats scissors!")
        else:
            print("you win!")








