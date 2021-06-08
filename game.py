import sys
import random
import time
from hats import hats

# QUESTIONS LIST --------------------------------------------------
q_file = open("questions.txt", "r")
content = q_file.read()
question_list = content.split("\n")
question_set = set(question_list)
q_file.close()

num_Qs = len(question_list)

# GAME STATUS CATEGORIES --------------------------------------------------
STATUS_PLAYING = "playing"
STATUS_FINISHED = "done"

# DEFAULT MESSAGES --------------------------------------------------
START = "MAGIC HAT"
INTRO = "Magic hat is a game you can play with your team. \nPick a question out of the hat!"


def get_question():
    """ Randomly selects question from questions list. """

    question = random.choice(question_list)

    return question


def show_hat():
    """ Displays a random hat image."""

    num = random.randint(0,(len(hats)-1))

    print(hats[num])


def retrieve_input(self):
    """ Get user input. """

    reply = input("> ").upper()

    return reply


class Game(object):
    """ A Magic Hat Game object. """

    def __init__(self):
        self.status = STATUS_PLAYING
        self.asked_Qs = set() # already asked questions
        self.auto_ask = False
        self.playing = True
        self.start_time = time.time()


    def start(self):
        """ Display the title and instructions of the game """

        print(START)
        show_hat()
        print(INTRO)

        return self.status


    def new_question(self):
        """ Display a new question that hasn't been asked yet.
        When all questions have been asked, reset."""

        # while len(self.asked_Qs) != 200:
        question = get_question()
        if question not in self.asked_Qs:
            self.asked_Qs.add(question)
            # print(question)
        else:
            question = get_question()

        return question


    def reset_questions(self):
        """When all questions have been asked, reset the set."""

        # if len(self.asked_Qs) != 200:
        if question_set == self.asked_Qs:
            self.asked_Qs = set()


    def get_status(self):
        """ Get the current status of gameplay. """

        return self.playing


def play_game():
    """ Initiate gameplay. """

    game = Game()
    game.start()

    while game.playing:
        print("\nDo you want to: ")
        print("1) Get a question, \n2) Turn on auto-ask, or \nQ) Quit?")
        choice = input("> ").upper()

        if choice == "1":
            print(game.new_question())
            # print("set:", game.asked_Qs)

        elif choice == "2":
            print("How often would you like to receive a question? Enter # of seconds:")
            seconds = int(input("> "))
            # while type(seconds) != int:
            #     seconds = input("Invalid length of time. Enter a # of seconds: \n> ")
            print(f"Magic Hat will ask a question every {seconds} seconds. \nType 'S' to stop auto-asking questions.\n")
            # starttime = time.time()
            game.auto_ask = True
            while game.auto_ask:
                print(get_question())
                time.sleep(seconds)
                # user_input = input()
                # if user_input.upper() == "S":
                #     game.auto_ask = False
                #     break

        elif choice == "Q":
            print("\nHope you enjoyed the questions! :)")
            game.playing = False
            game.status = STATUS_FINISHED
            return game.status

        else:
            print("\nYou can't do that with the magic hat!")


# def ticktock():
#     starttime = time.time()
#     while True:
#         print(time.time(), "tick")
#         seconds = 10.0
#         time.sleep(seconds - ((time.time() - starttime) % 60.0))


if __name__ == '__main__':
    # print(question_set)
    play_game()

    # ticktock()

    # game = Game()
    # print(game.asked_Qs)
    # game.new_question()
