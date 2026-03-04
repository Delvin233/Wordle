from letter_check import LetterCheck


class Wordle:

    MAX_ATTEMPTS = 6
    WORD_LENGTH = 6

    def __init__(self, secret: str):
        self.attempts = []
        self.secret: str = secret.upper()

    def attempt(self, word: str):
        word = word.upper()
        self.attempts.append(word)

    def guess_check(self, word: str):
        result = []
        word = word.upper()

        for i in range(self.WORD_LENGTH):

            character = word[i]
            letter = LetterCheck(character)
            letter.is_in_word = character in self.secret
            letter.is_in_position = character == self.secret[i]
            result.append(letter)

        return result

    @property  # this would enable us to call this as a variable than as a function
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret

    @property
    def remaining_attempts(self) -> int:
        return self.MAX_ATTEMPTS - len(self.attempts)

    @property  # this would enable us to call this like a variable than as a function
    # so we wont have to use the () when calling the function
    def can_attempt(self):
        return self.remaining_attempts > 0 and not self.is_solved

    # @property
    # def print_attempts(self):
    # return self.attempts
