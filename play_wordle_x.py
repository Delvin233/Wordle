from wordle_x import Wordle
from colorama import Fore
from typing import List
from letter_check import LetterCheck
import random


def main():
    word_set = load_word_set("data/wordle_words_six.txt")
    secret = random.choice(list(word_set))
    wordle = Wordle(secret)

    while wordle.can_attempt:
        user_input = input("What's your Guess: ")
        print("\n")

        if len(user_input) != wordle.WORD_LENGTH:
            print(
                Fore.RED
                + f"Word must be {wordle.WORD_LENGTH} characters long \n"
                + Fore.RESET
            )
            continue

        wordle.attempt(user_input)
        display_result(wordle)

        # debug check
        # print(*wordle.guess_check(user_input), sep="\n")

    if wordle.is_solved:
        print("Right Guess!")
    else:
        print("\nWrong Guess")
        print(f"The word was {wordle.secret}")


# helper function to load the owrds
def load_word_set(path: str):
    word_set = set()

    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set


# helper function to display reuslts
def display_result(wordle: Wordle):
    for word in wordle.attempts:
        result = wordle.guess_check(word)
        colored_result_str = convet_result_color(result)
        print(colored_result_str)
    for _ in range(wordle.remaining_attempts):
        print("_ " * wordle.WORD_LENGTH)


#  helper function to convert result to color codes
def convet_result_color(result: List[LetterCheck]):
    result_with_color = []
    color_reset = Fore.RESET

    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE

        colored_letter = color + letter.character + color_reset
        result_with_color.append(colored_letter)

    return " ".join(result_with_color)


if __name__ == "__main__":
    main()
