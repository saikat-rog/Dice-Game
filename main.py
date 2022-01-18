import random
ask = input("Do you want to play dice roll game? (y/n): ")
if ask.lower == "n":
    print("Sorry to see you go.")
else:
    print("Lets play")
    numer = input("Press any key to roll the dice.")
    if numer > 'a' or numer < 'z' or numer > 0 or numer < 0:
        rd = random.randint(1,6)
        if rd == 6:
            print(f"Hurray!! This is: {rd}")
        else:
            print(f"This is: {rd}")