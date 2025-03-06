rows = 16
columns = 60

def get_user_input():
    print("1. car \n2. jeep ")
    car = int(input("Enter your choice: "))
    wheels = int(input("Enter how many wheels you require (2 or 4): "))
    while car not in [1, 2] or wheels not in [2, 4]:
        print("Invalid input! Please enter again.")
        print("1. car \n2. jeep ")
        car = int(input("Enter your choice: "))
        wheels = int(input("Enter how many wheels you require (2 or 4): "))
    return car, wheels

def print_car(wheels):
    for i in range(rows):
        for j in range(columns):
            if (
                (i == 0 and 12 <= j <= 31) or
                (i == 1 and (j == 11 or j == 32)) or
                (i == 2 and (j == 10 or j == 33)) or
                (i == 3 and (j == 9 or j == 34)) or
                (4 <= i <= 7 and 0 <= j <= 49)
            ):
                print("*", end="")
            elif wheels == 2 and (
                ((i == 8 or i == 10) and (j == 8 or j == 10)) or
                (i == 9 and (7 <= j <= 11)) or
                ((i == 8 or i == 10) and (j == 38 or j == 40)) or
                (i == 9 and (37 <= j <= 41))
            ):
                print("*", end="")
            elif wheels == 4 and (
                ((i == 8 or i == 10) and (j == 5 or j == 8 or j == 13 or j == 16)) or
                (i == 9 and (4 <= j <= 9 or 12 <= j <= 17)) or
                ((i == 8 or i == 10) and (j == 35 or j == 38 or j == 43 or j == 46)) or
                (i == 9 and (34 <= j <= 39 or 42 <= j <= 47))
            ):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_jeep(wheels):
    for i in range(rows):
        for j in range(columns):
            if (
                (i == 0 and 10 <= j <= 45) or
                (i == 1 and (j == 8 or j == 46)) or
                (i == 2 and (j == 6 or j == 47)) or
                (i == 3 and 0 <= j <= 18) or
                (3 <= i <= 5 and 0 <= j <= 50) or
                (i == 6 and 0 <= j <= 51) or
                (i == 7 and 0 <= j <= 51)
            ):
                print("*", end="")
            elif wheels == 2 and (
                ((i == 8 or i == 10) and (j == 8 or j == 10)) or
                (i == 9 and (7 <= j <= 11)) or
                ((i == 8 or i == 10) and (j == 38 or j == 40)) or
                (i == 9 and (37 <= j <= 41))
            ):
                print("*", end="")
            elif wheels == 4 and (
                ((i == 8 or i == 10) and (j == 5 or j == 8 or j == 13 or j == 16)) or
                (i == 9 and (4 <= j <= 9 or 12 <= j <= 17)) or
                ((i == 8 or i == 10) and (j == 35 or j == 38 or j == 43 or j == 46)) or
                (i == 9 and (34 <= j <= 39 or 42 <= j <= 47))
            ):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def main():
    car, wheels = get_user_input()
    if car == 1:
        print_car(wheels)
    elif car == 2:
        print_jeep(wheels)

main()
