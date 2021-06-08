import sys
import random
import time
from hats import hats

# QUESTIONS LIST --------------------------------------------------
q_file = open("questions.txt", "r")
content = q_file.read()
question_list = content.split("\n")
q_file.close()


def get_question():
    """ Randomly selects question from questions list. """

    question = random.choice(question_list)

    return question


def show_hat():
    """ Displays a random hat image."""

    num = random.randint(0,(len(hats)-1))

    print(hats[num])


def play_game():
    """ Initiate gameplay. """

    print("Welcome to the MAGIC HAT!")
    show_hat()
    print("Magic hat is a game you can play with your team, where you pick a question out of a hat, as a team building exercise.")

    playing = True
    auto_ask = False
    asked_Qs = set()  # already asked questions

    while playing:
        print("\nDo you want to: ")
        print("1) Get a question, \n2) Turn on auto-ask, or \nQ) Quit?")
        choice = input("> ").upper()

        if choice == "1":
            print(get_question())

        elif choice == "2":
            print("How often would you like to receive a question? Enter # of seconds:")
            seconds = int(input("> "))

            print(f"Magic Hat will ask a question every {seconds} seconds. \nType 'S' to stop auto-asking questions.\n")
            auto_ask = True
            while auto_ask:
                print(get_question())
                time.sleep(seconds)

        elif choice == "Q":
            print("\nHope you enjoyed the questions! :)")
            playing = False

        else:
            print("\nYou can't do that with the magic hat!")



if __name__ == '__main__':
    play_game()
