import random

num_sides = 6

print("-------- Welcome to Dice Roller --------")
print(" ")
print("The rules of the game:")
print("  * You can only roll ONCE")
print("  * But if you roll a 6, you will win the prize to ROLL AGAIN!")
print(" ")
print("---> To Roll The Dice, Enter: roll")
print("---> To Exit, Enter: exit ")

while True:
    option = input("What's your option? " )

    if option == "roll":
        roll_function = random.randint(1, num_sides)
        if roll_function == 6:
            print("You rolled a", roll_function, "Congratulations! You won the prize and you can roll again!")
        else:
            print("You rolled a", roll_function)
            break

    elif option == "exit":
        break

    else:
        print("Invalid option. Please enter ' roll ' OR ' exit '.")