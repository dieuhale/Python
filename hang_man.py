import random # Imports the random module
import os #imports the os module

def clear():
    # Clear command as function of OS
    command = 'cls' if os.name in ('nt', 'dos') else 'clear'
    os.system(command)

# Initializes a list named stages
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

# Defines a multi-line string logo which contains the ASCII art representation of the game's title/logo.
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

# Initializes a list named word_list
word_list = [
    "Accelerate", "Analyze", "Atmosphere", "Bacteria", "Catalyst",
    "Chronological", "Comprehend", "Democracy", "Ecosystem", "Equation",
    "Fossilize", "Genre", "Hemisphere", "Hypothesis", "Illuminate",
    "Juxtapose", "Kinetic", "Latitude", "Metaphor", "Narrative",
    "Oxidation", "Parable", "Quarantine", "Renaissance", "Satire",
    "Theorem", "Unify", "Variable", "Wavelength", "Zenith",
    "Abstract", "Biodiversity", "Coefficient", "Dialogue", "Ethical",
    "Federal", "Genetic", "Heritage", "Inference", "Jurisdiction",
    "Kinship", "Legislature", "Molecule", "Neuron", "Osmosis",
    "Photosynthesis", "Quantum", "Resonance", "Syntax", "Topography"
]
         


chosen_word = random.choice(word_list) # Randomly selects a word from word_list
word_length = len(chosen_word) # Determines the length of chosen_word and assigns it to word_length.

end_of_game = False # Initializes a boolean variable end_of_game to False. This will be used to control the game loop.
lives = 6 # Sets the initial number of lives to 6.
guessed_letters = set() # Initializes an empty set to keep track of letters guessed by the player

print(logo) # Prints the game logo

# Initializes an empty list named display to hold the current state of the player's guesses.
display = []
for _ in range(word_length): # Loops through the length of the chosen word.
    display += "_" # Adds an underscore to the display list for each letter in the chosen word, representing unguessed letters.

while not end_of_game: # Starts the main game loop that will continue until end_of_game is True.
    guess = input("Guess a letter: ").lower() # Prompts the player to guess a letter and converts it to lowercase.

    clear() # Clears the screen

    if guess in guessed_letters: # Checks if the guessed letter has already been guessed before.
        print(f"You've already guessed {guess}") # Informs the player if they have already guessed the letter.
    else:
        guessed_letters.add(guess) # Adds the new guess to the set of guessed letters.

        for position in range(word_length): # Iterates through each position in the chosen word.
            letter = chosen_word[position] # Gets the letter at the current position.
            if letter == guess: # Checks if the letter at the current position matches the guessed letter.
                display[position] = letter # If the guessed letter is correct, updates the display list at the corresponding position.

        if guess not in chosen_word: # Checks if the guessed letter is not in the chosen word.
            print(f"You guessed {guess}, that's not in the word. You lose a life.") # Informs the player that their guess was incorrect and they lose a life.
            lives -= 1 # Decreases the lives count by one.
            if lives == 0: # Checks if the player has run out of lives.
                end_of_game = True # If lives are zero, sets end_of_game to True to end the game.
                print(f"You lose. The word is {chosen_word}.") # Informs the player that they have lost the game.

    print(f"{' '.join(display)}") # Prints the current state of display, showing correctly guessed letters and underscores for remaining letters.

    if "_" not in display: # Checks if there are no more underscores in display, indicating that all letters have been guessed correctly.
        end_of_game = True # If all letters are guessed, sets end_of_game to True.
        print("You win.") # Informs the player that they have won the game.

    print(stages[lives]) # Prints the current hangman stage based on the remaining number of lives.
    print(f"Lives remaining: {lives}") # Prints the number of lives remaining.
