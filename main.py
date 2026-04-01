

import random
import time
from words import words
from hangman_art import hangman_art
import string


def prints_ascii_art(number_of_wrong_guesses: int) -> None:
    """Prints ascii art according to the number of wrong guesses from the player.

    :param number_of_wrong_guesses: The number of wrong guesses of the player in the game.
    """
    print(hangman_art[number_of_wrong_guesses])


def loading() -> None:
    """Simulates a loading time.
    """
    print()
    num_points = random.randint(3, 10)
    for _ in range(num_points):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print()
    print()
    print("Well, I thought about a pretty awesome word! Can you find it?")


def generate_random_word() -> str:
    """Generates random word from list.

    :return: A random word from a list.
    """
    return random.choice(words)


def generate_word_mask(random_word: str) -> str:
    """Given a word generates its mask for the game

    :param random_word: A random word that the player has to get right
    :return: A mask of the word consisting in "_" in place of the word characters
    """
    return "_" * len(random_word)


def check_player_guess(guess: str, random_word: str, mask: str, guessed_letters: list[str], guess_number: int) -> tuple[str, int, list[str]]:
    """Check if the player input is in the random word and returns the updated mask and number of wrong guesses.
    
    :param guess: The guess that the player gave.
    :param random_word: The random word that the player has to find out.
    :param mask: The mask of the word.
    :param guessed_letters: The letters that the player has already guessed.
    :param guess_number: The number of guesses the player has given.

    :return: The updated mask, number of guesses and guessed letters
    """
    mask = list(mask)
    random_word = list(random_word)
    if guess not in string.ascii_letters or len(guess) != 1:
        print("You entered an invalid input! Try again!")
    elif guess in random_word and guess not in guessed_letters:
        for i in range(len(random_word)):
            if guess == random_word[i]:
                mask[i] = guess
        guessed_letters.append(guess)
    elif guess in guessed_letters:
        print(f"You already guessed the letter: {guess}! Try again!")
    else:
        print(f"The word does not have the letter {guess}! Try again")
        guessed_letters.append(guess)
        guess_number += 1
    return "".join(mask), guess_number, guessed_letters        


def main_game(number_of_guesses: int, random_word: str, mask: str) -> None:
    """The main engine of the game.

    :param number_of_guesses: The number of wrong guesses the player has given.
    :param random_word: A random word from a list that the player has to find out.
    :param mask: The mask of the random word with "_" in place of its characters.
    """
    guessed_letters = []
    while number_of_guesses < 6 and "_" in mask:
        prints_ascii_art(number_of_guesses)
        guess = input("Guess a letter:\n> ").replace(" ", "").lower()
        mask, number_of_guesses, guessed_letters = check_player_guess(guess, random_word, mask, guessed_letters, number_of_guesses)
        print(mask)
    if number_of_guesses == 6:
        prints_ascii_art(number_of_guesses)
        print(f"You lost! The word was: {random_word}! Better luck next time!")
    else:
        print("You win!!!")


    
def main():
    number_of_wrong_guesses = 0
    print("Welcome to the Hangman Game!")
    print("I am going to think about a word now!")
    loading()
    random_word = generate_random_word()
    mask_word = generate_word_mask(random_word)
    main_game(number_of_wrong_guesses, random_word, mask_word)




if __name__ == "__main__":
    main()