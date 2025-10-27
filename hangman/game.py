from data import words

def  secret_hiding(secret:str):
    return ['_' for i in range(len(secret))]

def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str]:
    return len(ch) == 1 and ch not in guessed

def request_input(guessed: set[str]):
    signal = input('Guess a letter from the secret word:')
    if not validate_guess(signal, guessed):
        return request_input()
    return signal

def end_of_game(display,secret,guessed):
    if '_' in display:
        return ('The tries are over!')
    else:
        return (f"""'You guessed the whole word!!!
                
                The word is: {secret}
                
                The letters you guessed are: {guessed}""")

def init_state(secret: str=None, max_tries: int=10) -> dict:
    if secret == None:
        secret = words.choose_secret_word()
    display = secret_hiding(secret)
    Correct_guesses = {set}
    wrong_guesses = {set}
    guessed = {set}
    return {
        'secret' : secret,
        'display' : display,
        'Correct_guesses' : Correct_guesses,
        'wrong_guesses' : wrong_guesses,
        'all guessed' : guessed,
        'max_tries' : max_tries
        }
    
def Game_mode(status:dict):
    secret = status['secret']
    display = status['display']
    guessed = status['all guessed']
    Correct_guesses = status['Correct_guesses']
    wrong_guesses = status['wrong_guesses']
    max_tries = status['max_tries']
    print (display)
    signal = request_input(guessed)
    while len(max_tries) > 0 and '_' in display:
        if signal in secret:
            print ('right!')
            guessed.append(signal)
            Correct_guesses.append(signal)
            display[secret.index(signal)] = signal
        elif signal not in secret:
            print ('wrong!')
            guessed.append(signal)
            wrong_guesses.append(signal)
            max_tries -= 1
    return end_of_game

Game_mode(init_state)
