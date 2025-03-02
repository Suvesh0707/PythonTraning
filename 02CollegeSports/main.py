print("Welcome to Indala College of Engineering")
print("Select \n 1. Hackathon \n 2.Cricket \n 3.Chess")
choice = int(input("Enter your choice: "))
age = int(input("Enter your age: "))


while True:
    if age < 18:
        print("You are kid, go and watch pogo")
        break
    else:
        if choice == 1:
            print("Go to Lab")
            break
        elif choice == 2:
            print("Go to Ground")
            break
        elif choice == 3:
            print("Go to Library")
            break
        else:
            choice = int(input("Enter Valid Input Again: "))