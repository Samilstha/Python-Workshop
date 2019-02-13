def marriage_point_calculator():
    a = str(input("Have you seen the joker or not? (Y/N)"))

    if a.lower()=="y":
        x = int(input("Your Maal: "))
        y = int(input("Total Maal: "))
        z = int(input("Total number of players:"))

        if x * z > y:
            return "You Win:", (x * z) - (y + 3)
        elif x * z < y:
            return "Your net loss is:", (y + 3) - (x * z)
    else:
        y = int(input("Total Maal: "))
        return "Your net loss is", (y + 10)

print(marriage_point_calculator())
