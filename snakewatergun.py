import random
from enum import IntEnum

# Enum for better readability
class Choice(IntEnum):
    SNAKE = 0
    WATER = 1
    GUN = 2

# Emoji representations
emojis = {
    'snake': '🐍',
    'water': '🌊',
    'gun': '🔫'
}

choice_map = {
    'snake': Choice.SNAKE,
    'water': Choice.WATER,
    'gun': Choice.GUN
}

# Outcome matrix: user vs computer
outcome_matrix = [
    [0, 1, -1],  # snake vs snake/water/gun
    [-1, 0, 1],  # water vs snake/water/gun
    [1, -1, 0]   # gun vs snake/water/gun
]

def get_user_choice():
    while True:
        print("Enter your choice (snake 🐍 / water 🌊 / gun 🔫):")
        user_input = input("➤ ").strip().lower()
        if user_input in choice_map:
            return user_input
        print("❗ Invalid choice! Please enter snake, water, or gun.")

def display_choices(user, computer):
    print(f"\n🧑 You chose: {emojis[user]}")
    print(f"💻 Computer chose: {emojis[computer]}")

def determine_winner(user_choice, computer_choice, user_won, computer_won, draws):
    user_idx = choice_map[user_choice]
    comp_idx = choice_map[computer_choice]
    result = outcome_matrix[user_idx][comp_idx]

    if result == 1:
        print("🎉 You Win!")
        user_won += 1
    elif result == -1:
        print("😞 You Lose!")
        computer_won += 1
    else:
        print("😐 It's a Draw!")
        draws += 1

    return user_won, computer_won, draws

def play_game():
    print("🎮 Welcome To The Snake 🐍 Water 🌊 Gun 🔫 Game!\n")

    count = 0
    user_won = 0
    computer_won = 0
    draws = 0

    while True:
        ask = input("\nDo you wanna play? (Y/N): ").strip().lower()

        if ask in ['y', 'yes']:
            user_choice = get_user_choice()
            computer_choice = random.choice(list(choice_map.keys()))

            count += 1
            display_choices(user_choice, computer_choice)

            user_won, computer_won, draws = determine_winner(
                user_choice, computer_choice, user_won, computer_won, draws
            )

        elif ask in ['n', 'no']:
            print("\n🙏 Thanks for playing!")
            break

        else:
            print("❗ Please enter 'Y' for Yes or 'N' for No.")

    # Final score summary
    print("\n📊 Game Summary:")
    print(f"Total rounds played: {count}")
    print(f"✅ You won: {user_won}")
    print(f"❌ Computer won: {computer_won}")
    print(f"😐 Draws: {draws}")

# Add KeyboardInterrupt handling
if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\n👋 Game interrupted. Goodbye!")