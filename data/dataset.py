import random

words = ["apples", "bottle", "breads"]
picked_words = []


def unique_word():
    if not words:
        return "WordBank Depleted"

    random_word = random.choice(words)
    picked_words.append(random_word)
    words.remove(random_word)

    return random_word


print(unique_word())
print(f"Remaining Words: {words}")
