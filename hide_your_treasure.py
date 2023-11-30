# Initializing each line of the map as a separate list
line1 = ["⬜️","️⬜️","️⬜️"]  # Represents the first row of the grid
line2 = ["⬜️","⬜️","️⬜️"]  # Represents the second row of the grid
line3 = ["⬜️️","⬜️️","⬜️️"]  # Represents the third row of the grid

# Combining the individual lines into a map (nested list)
map = [line1, line2, line3]  # Map is a list of lists forming a 3x3 grid

# Printing a message about the game
print("Hiding your treasure! X marks the spot.")

# Getting the user input for the treasure location
position = input()  # User enters where they want to put the treasure

# Processing the user input
letter = position[0].lower()  # Extracts the row letter and converts it to lowercase
abc = ["a", "b", "c"]  # List of letters corresponding to the rows
letter_index = abc.index(letter)  # Gets the index of the row letter

number_index = int(position[1]) - 1  # Converts the column number from string to int and adjusts for zero-based indexing

# Updating the map with the 'X' mark at the specified position
map[number_index][letter_index] = "X"  # Places an 'X' in the specified position

# Printing the updated map
print(f"{line1}\n{line2}\n{line3}")  # Displays each row of the map on a new line
