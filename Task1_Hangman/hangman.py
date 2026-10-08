import random

WORDS = ["python", "laptop", "coding", "school", "planet"]
MAX_INCORRECT_GUESSES = 6


def display_word(word, guessed_letters):
    """Return the current masked version of the word."""
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in word
    )


def get_guess(guessed_letters):
    """Get and validate one new letter from the player."""
    while True:
        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabetic letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        return guess


def play_game():
    word = random.choice(WORDS)
    guessed_letters = set()
    incorrect_guesses = 0

    print("\n" + "=" * 42)
    print("HANGMAN")
    print("=" * 42)
    print("Guess the hidden word one letter at a time.")
    print(f"You can make {MAX_INCORRECT_GUESSES} incorrect guesses.")

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        print("\n" + "-" * 42)
        print("Word:", display_word(word, guessed_letters))
        print("Used:", ", ".join(sorted(guessed_letters)) or "None")
        print(
            f"Incorrect guesses: {incorrect_guesses}/"
            f"{MAX_INCORRECT_GUESSES}"
        )

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print("✓ Nice! That letter is in the word.")

            if all(letter in guessed_letters for letter in word):
                print("\n🎉 Congratulations! You won!")
                print(f"The word was: {word}")
                return True
        else:
            incorrect_guesses += 1
            remaining = MAX_INCORRECT_GUESSES - incorrect_guesses
            print(f"✗ Not in the word. {remaining} incorrect guess(es) left.")

    print("\n💡 Game over!")
    print(f"The correct word was: {word}")
    return False


def main():
    wins = 0
    games = 0

    while True:
        games += 1
        if play_game():
            wins += 1

        print(f"\nSession score: {wins}/{games} wins")
        choice = input("Play another round? (y/n): ").strip().lower()

        if choice != "y":
            print("\nThanks for playing Hangman!")
            print(f"Final score: {wins} win(s) out of {games} game(s).")
            break


if __name__ == "__main__":
    main()
