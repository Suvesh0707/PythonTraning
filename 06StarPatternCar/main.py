rows = 13
columns = 40
print("1. car \n2. jeep")
car = int(input("Enter your choice: "))

if car == 1:
    for i in range(rows):
        for j in range(columns):
            if (
                (i == 0 and 10 <= j <= 29) or
                (i == 1 and (j == 9 or j == 30)) or
                (i == 2 and (8 <= j <= 31)) or
                (i == 3 and (7 <= j <= 32)) or
                (4 <= i <= 7 and (2 <= j <= 37)) or
                ((i == 8 or i == 10) and (j == 5 or j == 7 or j == 29 or j == 31)) or 
                (i == 9 and (4 <= j <= 8 or 28 <= j <= 32))
            ):
                print("*", end="")
            else:
                print(" ", end="")
        print()

elif car == 2:
    for i in range(rows):
        for j in range(columns):
            if (
                (4 <= i <= 6 and 4 <= j <= 20) or
                (7 <= i <= 9 and 4 <= j <= 30) or
                (i == 10 and (j == 6 or j == 9 or j == 22 or j == 25)) or
                (i == 11 and (5 <= j <= 10 or 21 <= j <= 26)) or
                (i == 12 and (j == 6 or j == 9 or j == 22 or j == 25))
            ):
                print("*", end="")
            else:
                print(" ", end="")
        print()

else:
    print("Invalid input")
