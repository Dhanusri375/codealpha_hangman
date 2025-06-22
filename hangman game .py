import random

# List of predefined words
word_list = ["apple", "train", "house", "table", "chair"]

# Choose a random word from the list
secret_word = random.choice(word_list)
guessed_letters = []
attempts_left = 6

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("_ " * len(secret_word))

# Game loop
while attempts_left > 0:
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Correct!")
    else:
        attempts_left -= 1
        print(f"❌ Incorrect! Attempts left: {attempts_left}")

    # Show current state of the word
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\n" + display_word.strip())

    # Check win condition
    if all(letter in guessed_letters for letter in secret_word):
        print("🎉 Congratulations! You guessed the word:", secret_word)
        break

# If loop ends and word wasn't guessed
if attempts_left == 0:
    print("😢 Game Over! The word was:", secret_word)
