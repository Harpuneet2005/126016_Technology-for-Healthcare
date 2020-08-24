import random 
a1 = str(input("What is the First Letter of your name?  "))
n = int(input("When Is your Birthday (enter the date only)  "))
x = int(input("Please enter your age   "))
z = str(input("Do u have any co-morbidities or any chronic underlying disease(Answer with a Yes or No   "))
if x > 65:
    if z == "Yes":
        a4 = 1
    else:
        a4 = random.randint(1, 10)
else:
    if z == "Yes":
        a4 = 1
    else:    
        if a1 == "A":
            a2 = 1 * n
        elif a1 == "B":
            a2 = 2 * n
        elif a1 == "C":
            a2 = 3 * n
        elif a1 == "D":
            a2 = 4 * n
        elif a1 == "E":
            a2 = 5 * n
        elif a1 == "F":
            a2 = 6 * n
        elif a1 == "G":
            a2 = 7 * n
        elif a1 == "H":
            a2 = 8 * n
        elif a1 == "I":
            a2 = 9 * n
        elif a1 == "J":
            a2 = 10 * n
        elif a1 == "K":
            a2 = 11 * n
        elif a1 == "L":
            a2 = 12 * n
        elif a1 == "M":
            a2 = 13 * n
        elif a1 == "N":
            a2 = 14 * n
        elif a1 == "O":
            a2 = 15 * n
        elif a1 == "P":
            a2 = 16 * n
        elif a1 == "Q":
            a2 = 17 * n
        elif a1 == "R":
            a2 = 18 * n
        elif a1 == "S":
            a2 = 19 * n
        elif a1 == "T":
            a2 = 20 * n
        elif a1 == "U":
            a2 = 21 * n
        elif a1 == "V":
            a2 = 22 * n
        elif a1 == "W":
            a2 = 23 * n
        elif a1 == "X":
            a2 = 24 * n
        elif a1 == "Y":
            a2 = 25 * n
        elif a1 == "Z":
            a2 = 26 * n
        else:
            print("Invalid Option")
        a3 = a2/26
        a4=round(a3, 0)
print("U shall recieve the vaccine on", a4,"of January")


