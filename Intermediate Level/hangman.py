import random

# List of words
words = ["python", "computer", "hangman", "programming", "developer"]

# Randomly choose a word
word = random.choice(words)

guessed_letters = []
attempts = 6

# Hint
print("Hint: It is related to computers/programming.")

# Display function
def display_word():
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

# Game loop
while attempts > 0:
    print("\nWord:", display_word())
    print("Attempts left:", attempts)

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong guess!")

    # Visual Progress
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]

    print(stages[6 - attempts])

    # Check win condition
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You guessed the word:", word)
        break

# Lose condition
if attempts == 0:
    print("\nGame Over! The word was:", word)