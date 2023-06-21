"""
An implementation of the game Hangman.

Author: James LaFarr
Version: 12.22.22
"""
from english_words import get_english_words_set
from random import choice


def print_greeting() -> None:
    print('Welcome to hangman. You have 10 wrong guesses to guess my word.')
    print('Good luck. You\'re going to need it!')


class Hangman:
    def __init__(self):
        self._word: str = choice(list(get_english_words_set(['web2'], lower=True)))
        self._lives_left: int = 5
        self._correct_guesses = 0
        self._letters_guessed: list[str] = list()
        self._play()

    def print_wordbank(self):
        print(f"You have guessed the following letters: {self._letters_guessed}")

    def _guess(self, letter: str) -> bool:
        correct: bool = letter in self._word
        self._letters_guessed.append(letter)
        if correct:
            self._correct_guesses += 1
        else:
            self._lives_left -= 1
        return correct

    def valid_guess(self, letter: str):
        if letter in self._letters_guessed or len(letter) != 1:
            return False
        return True

    def _print_partial_word(self):
        partial_word: str = ""
        for letter in self._word:
            if letter in self._letters_guessed:
                partial_word += letter + ' '
            else:
                partial_word += "_ "
        print(partial_word)

    def _play(self):
        print(self._word)
        print_greeting()
        while self._lives_left > 0:
            self._print_partial_word()
            self.print_wordbank()
            guess: str = input("What is your guess? ")
            while not self.valid_guess(guess):
                guess = input("Guess is invalid: ")
            correct = self._guess(guess)
            count: int = 0
            for letter in self._word:
                if letter in self._letters_guessed:
                    count += 1
            win: bool = count == len(self._word)
            if win:
                break
            elif correct:
                print(f"Correct. There are {len(self._word) - self._correct_guesses} left.")
            else:
                print(f"Wrong! You now have {self._lives_left} lives left")
        if self._lives_left <= 0:
            print(f"You lost. I knew you were stupid. My word was {self._word}. I knew you wouldn't get it.")
        else:
            print(f"Damn. You will never beat me again.")
