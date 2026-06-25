import random

# ---------------------------------------
# Word Guess Challenge (Hangman Style)
# ---------------------------------------

# List of possible secret words
words = [
    "python",
    "guitar",
    "keyboard",
    "computer",
    "banana",
    "football",
    "elephant",
    "notebook"
]

# Pick a random secret word
secret_word = random.choice(words)

# Game settings
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6


# Function to build the progress display
def build_progress(secret, guesses):
    progress = ""

    for letter in secret:
        if letter in guesses:
            progress += letter + " "
        else:
            progress += "_ "

    return progress.strip()


# Function to check if the word is fully guessed
def is_word_guessed(secret, guesses):
    for letter in secret:
        if letter not in guesses:
            return False

    return True


print("Welcome to the Word Guess Challenge!")
print(f"You have {max_wrong_guesses} wrong guesses available.\n")

# Main game loop
while wrong_guesses < max_wrong_guesses:

    # Show current progress
    print("Word:", build_progress(secret_word, guessed_letters))
    print("Guessed letters:", guessed_letters)
    print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)

    # Ask player for input
    guess = input("\nGuess a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter ONE letter only.\n")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    # Save the guessed letter
    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in secret_word:
        print("Correct!\n")
    else:
        wrong_guesses += 1
        print("Wrong guess!\n")

    # Check for win
    if is_word_guessed(secret_word, guessed_letters):
        print("Word:", build_progress(secret_word, guessed_letters))
        print("\nCongratulations! You guessed the word!")
        break

# Check for loss
if not is_word_guessed(secret_word, guessed_letters):
    print("\nYou ran out of guesses.")
    print("The secret word was:", secret_word)
