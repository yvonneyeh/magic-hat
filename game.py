import random
import time
import keyboard
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
MOVE_QUERY = "\nDo you want to: \n1) Get a question, \n2) Turn on auto-ask, or \nQ) Quit?"
TIME_QUERY = "\nHow often would you like to receive a question? Enter # of seconds:"
TIME_ERROR = "Sorry, I didn't understand that. Enter # of seconds:"
AUTO_OFF = "\nTurned off auto-ask!"
ENDING = "\nHope you enjoyed the questions with your team! :)"
BAD_MOVE = "\nThe magic hat does not understand your request!"


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
    """ A Magic Hat Game object. (game.Game)

    Methods:
    start: Begin the game (bool)
    get_question_from_list: Get a unique question.
    reset_questions: Reset question set once all 200 questions have been asked.
    get_status: Get status of gameplay (bool)

    """

    def __init__(self):
        self.status = STATUS_PLAYING
        self.Q_list = question_list.copy()
        self.new_Qs = set(question_list)
        self.asked_Qs = set()   # already asked questions
        self.auto_ask = False   # periodic questions
        self.playing = True     # game in progress
        self.start_time = time.time()


    def start(self):
        """ Display the title and instructions of the game """

        print(START)
        show_hat()
        print(INTRO)

        return self.status

    def get_question_from_list(self):
        """ Randomly selects question from questions list.
        Display a new question that hasn't been asked yet.
        When all questions have been asked, reset the set."""

        if len(self.Q_list) != 0 and not self.all_asked_already():
            question = random.choice(self.Q_list)
            self.Q_list.remove(question)
            self.asked_Qs.add(question)
        else:
            self.reset_questions()

        return question


    def get_new_question(self):
        """ Display a new question that hasn't been asked yet.
        When all questions have been asked, reset the set."""

        question = self.get_question_from_list()

        if not self.all_asked_already():

            # print("askedQs type",type(self.asked_Qs))
            if question not in self.asked_Qs:
                self.asked_Qs.add(question)
                # print(question)

            else:   # generate a previously unasked question
                question = self.get_question_from_list()

        else:
            self.reset_questions()

        return question


    def all_asked_already(self):
        """ Return true if all questions have been asked already. """

        return question_set == self.asked_Qs


    def reset_questions(self):
        """When all questions have been asked, reset the list."""

        # if len(self.asked_Qs) != 200:
        # if question_set == self.asked_Qs:
        self.Q_list = question_list.copy()

        return self.asked_Qs


    def get_status(self):
        """ Get the current status of gameplay. """

        return self.playing


def play_game():
    """ Initiate gameplay. """

    game = Game()
    game.start()

    while game.playing:
        print(MOVE_QUERY)
        choice = input("> ").upper()

        if choice == "1":
            print(game.get_question_from_list())

        elif choice == "2":
            print(TIME_QUERY)
            while True:
                try:
                    seconds = int(input("> "))
                except ValueError:
                    print(TIME_ERROR)
                    continue    # Try again... Return to the start of the loop.
                else:
                    break   # Seconds successfully parsed! Exiting the loop.
            print(f"Magic Hat will ask a question every {seconds} seconds. \nType 'S' to stop auto-asking questions.\n")
            game.auto_ask = True
            while game.auto_ask:
                print("\n",game.get_question_from_list())
                time.sleep(seconds)

                if keyboard.is_pressed("s"):
                    print(AUTO_OFF)
                    game.auto_ask = False
                    break

        elif choice == "Q":
            print(ENDING)
            game.playing = False
            game.status = STATUS_FINISHED
            return game.status

        else:
            print(BAD_MOVE)


if __name__ == '__main__':
    play_game()
