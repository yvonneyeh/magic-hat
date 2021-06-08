import re
import random
import string
from time import time, sleep
from hats import hats

# QUESTIONS LIST --------------------------------------------------
q_file = open("questions.txt", "r")
content = q_file.read()
question_list = content.split("\n")
q_file.close()

# GAME STATUS CATEGORIES --------------------------------------------------
STATUS_PLAYING = "playing"
STATUS_FINISHED = "done"

# DEFAULT MESSAGES --------------------------------------------------
INTRO = "Magic hat is a game you can play with your team, where you pick a question out of a hat, as a team building exercise."


def get_question():
    """ Randomly selects question from questions list. """

    question = random.choice(question_list)

    return question


def show_hat():
    """ Displays a random hat image."""

    num = random.randint(0,6)

    print(hats[num])


class Game(object):
    """ A Magic Hat Game object. """

    def __init__(self, word):
        self.status = STATUS_PLAYING
        self.asked_Qs = set() # already asked questions
        self.auto_ask = False
        self.start_time = time.time()


    def start():
        """ Display the title and instructions of the game """

        print(INTRO)


    def retrieve_input(self):
        """ Get user input. """

        reply = input('')

        return reply

    def new_question(self):
        """ Display a new question that hasn't been asked.
        When all questions have been asked, reset."""

        while len(asked_Qs) != 200:
            get_question()
            if question not in asked_Qs:
                asked_Qs.add(question)

        asked_Qs = set()

def play_game():
    """ Initiate gameplay. """

    game = Game()
    game.start()

    while True:
        print("\nDo you want to: ")
        print("1) Get a question, 2) Turn on periodic questions, 3) Turn off the periodic questions, or Q)uit?")
        choice = input("> ").upper()

        if choice == "1":
            get_question()

        elif choice == "2":
            get_question()

        elif choice == "3":
            get_question()

        elif choice == "Q":
            print("\nHope you enjoyed the questions! :)")
            break

        else:
            print("You can't do that with the magic hat!")


def ticktock():
    starttime = time.time()
    # while True:
    #     print(time.time(), "tick")
    #     time.sleep(60.0 - ((time.time() - starttime) % 60.0))

    while True:
        seconds = input("")
        time.sleep(60 - ((time.time() - starttime) % 60)
    	# thing to run

if __name__ == '__main__':
    # play_game()
    # ticktock()
