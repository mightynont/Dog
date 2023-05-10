import random

# List of words to use in the game
words = ['python', 'programming', 'computer', 'science', 'algorithm', 'data', 'code']

# Select a random word from the list
word = random.choice(words)

# Create a list of underscores to represent the hidden word
display = ['_'] * len(word)

# Set up the hangman
hangman = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]

# Set up variables for the game loop
incorrect_guesses = 0
max_guesses = len(hangman) - 1
letters_guessed = []

# Game loop
while True:
    # Print the hangman and the hidden word
    print(hangman[incorrect_guesses])
    print(' '.join(display))

    # Get the player's guess
    guess = input('Guess a letter: ').lower()

    # Check if the guess is valid
    if len(guess) != 1 or not guess.isalpha():
        print('Invalid guess. Please guess a single letter.')
        continue
    elif guess in letters_guessed:
        print('You already guessed that letter. Please guess another letter.')
        continue

    # Add the guess to the list of letters guessed
    letters_guessed.append(guess)

    # Check if the guess is in the word
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        incorrect_guesses += 1

    # Check if the game is over
    if ''.join(display) == word:
        print('You win! The word was', word)
        break
    elif incorrect_guesses == max_guesses:
        print('You lose! The word was', word)
        print(hangman[incorrect_guesses])
        break