# ASCII art for the rock option
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# ASCII art for the paper option
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

# ASCII art for the scissors option
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Store the ASCII art in a list for easy access
game_images = [rock, paper, scissors]

# Import the random module to use for generating the computer's choice
import random

# Prompt the user to make a choice
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

# Convert user input to an integer and store it in user_choice
user_choice = int(input()) 

# Loop for input validation
while True:
    try:
        # Check if the user's choice is within the valid range
        if 0 <= user_choice <= 2:
            break  # Exit loop if input is valid
        else:
            # Inform the user their input is out of range and prompt again
            print("Number out of range. Please enter 0, 1, or 2.")
    except ValueError:
        # Inform the user of an invalid input and prompt again
        print("Invalid input! Please enter a whole number.")

# Print the ASCII art corresponding to the user's choice
print(game_images[user_choice])

# Generate a random choice for the computer
computer_choice = random.randint(0, 2)
# Display the computer's choice
print(f"Computer chose: {computer_choice}")

# Print the ASCII art for the computer's choice
print(game_images[computer_choice])

# Determine the outcome of the game
if user_choice == computer_choice:
    # Print the outcome if both choices are the same
    print("It's a draw!")
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 2 and computer_choice == 1) or \
     (user_choice == 1 and computer_choice == 0):
    # Print the outcome if the user wins
    print("You win!")
else:
    # Print the outcome if the user loses
    print("You lose!")
