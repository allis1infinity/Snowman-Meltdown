import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")



def play_game():
    secret_word = get_random_word()
    mistakes = 0
    guessed_letters = []

    print("Welcome to Snowman Meltdown!")

    while mistakes < len(STAGES)-1 and not all(letter in guessed_letters for letter in secret_word):
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower()
        if guess in secret_word:
            guessed_letters.append(guess)
            print(guessed_letters)
        else:
            mistakes += 1
            print("OOOPS!")

    if mistakes == len(STAGES) -1:
        print("🫣The Snowman melted down...")
    else:
        print("You saved the Snowman, hooray!👌🥳")

    print(f"The secret word was: '{secret_word}'")


if __name__ == "__main__":
    play_game()