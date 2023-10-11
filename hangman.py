import random

WORDS = ['python', 'java', 'javascript', 'ithsai', 'pandas']

def menu():
    opt = get_option()
    while opt != "exit":
        print("H A N G M A N")
        play()
        opt = get_option()
    print("Goodbye!")

def get_option():
    opt = ''
    while not (opt == 'exit' or opt == 'play'):
        opt = input('Type "play" to play the game, "exit" to quit: ')
    return opt

def get_letter(guessed):
    print_guessed(guessed)
    valid_letter = input("Input a letter: ").strip()
    while not (is_valid_letter(valid_letter)):
        print_guessed(guessed)
        valid_letter = input("Input a letter: ").strip()
    return valid_letter

def is_valid_letter(valid_letter):
    if len(valid_letter) != 1:
        print("You should input a single letter")
        return False
    if not (valid_letter.isascii() and valid_letter.islower()):
        print("It is not an ASCII lowercase letter")
        return False
    return True

def print_guessed(guessed):
    print("".join(guessed))

def play():
    correct_word = random.choice(WORDS)
    remaining_tries = 8
    guessed = list("-" * len(correct_word))
    past_letters = set()

    while remaining_tries > 0 and "-" in guessed:
        print(f"Remaining tries: {remaining_tries}")
        letter = get_letter(guessed)
        letter_qt = correct_word.count(letter)
        if letter in past_letters:
            print("You already typed this letter")
        elif letter_qt == 0:
            print("No such letter in the word")
            remaining_tries = remaining_tries - 1
        else:
            idx = correct_word.find(letter)
            while idx > -1:
                guessed[idx] = letter
                idx = correct_word.find(letter, idx + 1)
        past_letters.add(letter)

    if "-" not in guessed:
        print("You guessed the word '" + correct_word + "'!")
        print("You survived!")
    else:
        print("You are hanged!")
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play()

if __name__ == '__main__':
    menu()
