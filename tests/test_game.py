import random

words = ["בננה", "תפוח", "חציל", "עגבניה", "מלפפון", "מחשב", "עכבר", "מקלדת", "מסך", "טלפון"
,"חלון", "דלת", "קיר", "שולחן", "כיסא", "מחברת", "עט", "עיפרון", "תיק", "ספר"
,"אוטובוס", "מכונית", "מטוס", "סירה", "אופניים", "רכבת", "כביש", "מפה", "עיר", "כפר"
,"מדבר", "יער", "ים", "הר", "שלג", "גשם", "שמש", "ירח", "כוכב", "שמיים"
,"חולצה", "מכנסיים", "נעליים", "גרביים", "מעיל", "כובע", "צעיף", "מטריה", "שעון", "משקפיים"
,"חתול", "כלב", "דג", "ציפור", "סוס", "כבשה", "עז", "פרה", "תרנגולת", "ברווז"
,"נמר", "פיל", "קוף", "אריה", "דוב", "גמל", "שועל", "זאב", "תן", "ינשוף"
,"פרח", "עלה", "עץ", "שיח", "דשא", "אבן", "נהר", "אגם", "מפלים", "מדורה"
,"מים", "חול", "אדמה", "שמיים", "רוח", "ברק", "ענן", "סערה", "קשת", "שלולית"
,"רופא", "מורה", "נהג", "כבאי", "שוטר", "חייל", "טבח", "חקלאי", "אופה", "מנקה"
,"צייר", "מוזיקאי", "נגר", "חשמלאי", "מדען", "סופר", "מהנדס", "צלם", "תלמיד", "מאמן"
,"שמחה", "עצב", "פחד", "אהבה", "כעס", "התרגשות", "שעמום", "תקווה", "דאגה", "שלווה"
,"לחם", "גבינה", "ביצה", "חמאה", "שוקולד", "עוגה", "גלידה", "קפה", "תה", "פיצה"
,"סוכר", "מלח", "פלפל", "בצל", "שום", "קמח", "אורז", "מרק", "חלב", "עוף"
,"אוניה", "רכב", "אופנוע", "מסוק", "מטען", "נמל", "תחנה", "כביש", "מחלף", "מנהרה"
"בית", "בניין", "מדרגות", "קומה", "גג", "חדר", "מטבח", "אמבטיה", "שירותים", "סלון"]

def choose_secret_word(words: list[str]) -> str:
    return (words[random.randrange(len(words))])

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

def init_state(secret: str=None, max_tries:int=10) -> dict:
    if secret == None:
        secret = choose_secret_word(words)[::-1]
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
        print ('display:', display)
        print ('guessed:', guessed)
        print ('Correct_guesses:', Correct_guesses)
        print ('wrong_guesses:', wrong_guesses)
        print ('max_tries:', max_tries)

    return end_of_game(display,secret,guessed)

print(Game_mode(init_state()))


