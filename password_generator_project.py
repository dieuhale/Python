# Import the random module for random operations
import random

# Define lists for possible characters in the password: letters, numbers, and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Print a welcome message for the password generator
print("Welcome to the PyPassword Generator!")

# Get user input for the number of letters, symbols, and numbers in the password
num_letters = int(input("How many letters would you like in your password?\n")) 
num_symbols = int(input(f"How many symbols would you like?\n"))
num_numbers = int(input(f"How many numbers would you like?\n"))

# Initialize the password variable (no longer needed as a number, so it's removed)
selected_letters = random.sample(letters, num_letters)
selected_numbers = random.sample(numbers, num_numbers)
selected_symbols = random.sample(symbols, num_symbols)

# Combine the selected characters into one list
combined_chars = selected_letters + selected_numbers + selected_symbols

# Shuffle the combined list to randomize the password
shuffled_password = random.sample(combined_chars, len(combined_chars))

# Initialize an empty string to hold the final password
final_password = ""

# Concatenate each character to form the final password string
for item in shuffled_password:
    final_password += item

# Print the final generated password
print(final_password)
