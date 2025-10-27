import random
from hangman import words

def secret_hiding(secret:str):
    return ['_' for i in range(len(secret))]

def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str]:
    return len(ch) == 1 and ch not in guessed and ch.isalpha()

def request_input(guessed: set[str]):
    signal = input('Guess a letter from the secret word:')
    if not validate_guess(signal, guessed):
        return request_input(guessed)
    return signal

def letter_revealing(guess:str, secret:str, display:list[str]):
    for signal in range(len(secret)):
        if secret[signal] == guess:
            display[signal] = guess
    return 
    

def end_of_game(display,secret,guessed):
    if '_' in display:
        print ('The tries are over!')
    else:
        print (f"""'You guessed the whole word!!!\nThe word is: {secret}\nThe letters you guessed are: {guessed}\n""")
    return

def init_state(secret: str=None, max_tries:int=10) -> dict:
    if secret == None:
        secret = words.choose_secret_word(words.words)[::-1]
    display = secret_hiding(secret)
    Correct_guesses = {set[str]}
    wrong_guesses = {set[str]}
    guessed = {set[str]}
    return {
        'secret' : secret,
        'display' : display,
        'Correct_guesses' : Correct_guesses,
        'wrong_guesses' : wrong_guesses,
        'all guessed' : guessed,
        'max_tries' : max_tries
        }
    
def game_mode(status:dict):
    secret = status['secret']
    print (secret)
    display = status['display']
    guessed = status['all guessed']
    Correct_guesses = status['Correct_guesses']
    wrong_guesses = status['wrong_guesses']
    max_tries = status['max_tries']
    print (display)
    while max_tries > 0 and '_' in display:
        signal = request_input(wrong_guesses)
        if signal in secret:
            print ('right!')
            guessed.add(signal)
            Correct_guesses.add(signal)
            letter_revealing(signal,secret,display)
        elif signal not in secret:
            print ('wrong!')
            guessed.add(signal)
            wrong_guesses.add(signal)
        max_tries -= 1
        print('--------------------------------')
        print ('display:', display)
        print ('guessed:', guessed)
        print ('Correct_guesses:', Correct_guesses)
        print ('wrong_guesses:', wrong_guesses)
        print ('max_tries:', max_tries)
        print('--------------------------------')

    return end_of_game(display,secret,guessed)


