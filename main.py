#HANGMAN in python
import random
from wordslist import words


hangman_art = {0: ("   ",
                   "   ",
                   "   ",),
               1: (" o ",
                   "   ",
                   "   ",),
               2: (" o ",
                   " | ",
                   "   ",),
               3: (" o ",
                   "/| ",
                   "   ",),
               4: (" o ",
                   "/|\\",
                   "   ",),
               5: (" o ",
                   "/|\\",
                   "/  ",),
               6: (" o ",
                   "/|\\",
                   "/ \\",)}

#this function displays the hangman drawing;
#a part of the hangman gets displayed if the user answers wrong
def display_man(wrong_guesses):
    print("*********")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**********")

# this functions displays a hit "_ _ _ _ _"
def display_hint(hint):
    print(" ".join(hint))

#this functions displays the answer
def display_answer(answer):
    print(" ".join(answer))

# this is the main function of the program
def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        #this is an edge case where a user can only guess a letter and no input the whole word
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!!")
            is_running = False


if __name__ == "__main__":
    main()
