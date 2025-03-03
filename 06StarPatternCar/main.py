
rows = 12
columns = 40

for i in range(rows):
    for j in range(columns):
        if (
            (i == 0 and 10 <= j <= 29) or
            (i == 1 and (j == 9 or j == 30)) or
            (i == 2 and (8 <= j <= 31)) or
            (i == 3 and (7 <= j <= 32)) or
            
            (i == 2 and (j == 13 or j == 20 or j == 27)) or
            (i == 3 and (j == 13 or j == 20 or j == 27)) or
            
            (4 <= i <= 7 and (j >= 2 and j <= 37)) or
            
            ((i == 8 or i == 10) and (j == 5 or j == 7 or j == 29 or j == 31)) or 
            (i == 9 and (4 <= j <= 8 or 28 <= j <= 32)) 
        ):
            print("*", end="")
        else:
            print(" ", end="")
    print()  
