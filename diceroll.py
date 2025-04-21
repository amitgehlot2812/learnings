import random

def roll_dice(num_rolls):
    return [random.randint(1,6) for _ in range(num_rolls)]

def main():
    print("🎲 Welcome to the Dice Rolling Game")
    count = 0

    while True: 
        choice = input("Do you wanna play? (Y/N): ").strip().lower()

        if choice == 'y':
            try:
                number_of_rolls = int(input("How many dice to roll: "))
                if number_of_rolls <= 0:
                    print("Enter a number greater than 0.")
                    continue
            except ValueError:
                print("⚠️ Please enter a valid number.")
                continue

            rolls = roll_dice(number_of_rolls)
            print(f"🎲 Dice rolled: {rolls}")
            print(f" Total: {sum(rolls)} | Average: {sum(rolls)/len(rolls):.2f}")
            count += 1

        elif choice == 'n':
            print("Thank you for playing")
            break 
        
        else:
            print("❗Please enter 'Y' for Yes or 'N' for No.")
    
    print(f"🧾 You played the game {count} time(s).")

if __name__ =='__main__':
    main()

# print("Welcome to the game.")
# count = 0 #counter for how many times game played

# while True: #finite for yes and no to terminate
#     choice = input("Do you wanna play? (Y/N): ").lower()

#     if choice == 'y':
#         diceroll = [] #list to store number of time dice roll
#         try:
#             number_of_rolls = int(input("How many dice to roll: "))
#         except ValueError:
#             print("Please enter a valid number.")
#             continue
#         for x in range(number_of_rolls): #loop to roll dice as user input
#             dice1 = random.randint(1,6) #generate random number for dice
#             diceroll.append(dice1) #storing dice number to empty list 
#         print(diceroll) # printing list
#     elif choice == 'n':
#         print("Thank you for playing")
#         break #break the while loop if no to play
#     else:
#         print("Enter valid choice.")
#     count += 1 #increament counter by 1 to number time game played. 
# print(f"You played the game {count} times.") #print how many time game played
# print(f"Dice rolls: {diceroll}")
# print(f"Total: {sum(diceroll)} | Average: {sum(diceroll)/len(diceroll):.2f}")
