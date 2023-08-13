import random

def hangman_game():
    words = ["apple", "banana", "cherry", "dog", "elephant", "frog", "grape", "horse", "iguana", "jaguar"]
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    def display_word():
        display = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display += letter
            else:
                display += "_"
        return display

    print("Welcome to Hangman!")
    print(display_word())

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in secret_word:
            guessed_letters.append(guess)
            print(display_word())
            if "_" not in display_word():
                print(f"Congratulations! You guessed the word '{secret_word}' correctly.")
                break
        else:
            guessed_letters.append(guess)
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
            print(display_word())

    if "_" in display_word():
        print(f"Sorry, you lost. The word was '{secret_word}'.")

hangman_game()
