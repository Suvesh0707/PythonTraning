elif car == 2:
    # Jeep Design
    for i in range(rows):
        for j in range(columns):
            if (
                (i == 4 and 4 <= j <= 40) or
                ((i == 5 or i == 6) and ( j== 4 or j == 40) ) or
                ((i == 7) and ( j== 4 or j == 40) ) or
                (7 <= i <= 10 and 4 <= j <= 50)
            ):
                print("*", end="")
            
            # Wheels condition for the jeep
            elif wheels == 2 and (
                # Two-wheel design
                ((i == 11 or i == 13) and (j == 6 or j == 9 or j == 22 or j == 25)) or
                (i == 12 and (5 <= j <= 10 or 21 <= j <= 26)) 
            ):
                print("*", end="")
            
            elif wheels == 4 and (
                # Four-wheel design (adding extra wheels)
                (i == 10 and (j == 4 or j == 6 or j == 9 or j == 11 or j == 22 or j == 25 or j == 28 or j == 30)) or
                (i == 11 and (3 <= j <= 12 or 21 <= j <= 32)) or
                (i == 12 and (j == 4 or j == 6 or j == 9 or j == 11 or j == 22 or j == 25 or j == 28 or j == 30))
            ):
                print("*", end="")
            
            else:
                print(" ", end="")
        print()
