import random

def choose_secret_word(words: list[str]) -> str:
    choose = random.randrange(len(words))
    return (words[choose])


