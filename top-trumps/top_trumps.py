<<<<<<< HEAD
import random
import json

with open('cards.json') as f:
    cards = json.load(f)

player_card = random.choice(cards)
computer_card = random.choice(cards)

print("\nYour card:")
for stat, value in player_card.items():
    print(f"{stat.title()}: {value}")

valid_stats = [stat for stat in player_card if stat != "name"]
chosen_stat = ""

while chosen_stat not in valid_stats:
    chosen_stat = input(f"\nChoose a stat to compare ({', '.join(valid_stats)}): ").lower()

player_val = player_card[chosen_stat]
computer_val = computer_card[chosen_stat]

print(f"\nComputer card: {computer_card['name']} - {chosen_stat.title()}: {computer_val}")

if player_val > computer_val:
    print("You win!")
elif player_val < computer_val:
    print("You lose.")
else:
    print("It's a draw.")
=======

>>>>>>> d1a55a26426084ebda2af9a1ade47ab803bf8026
