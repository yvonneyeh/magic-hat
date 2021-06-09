import random
import time
import keyboard
from hats import hats


# QUESTIONS LIST --------------------------------------------------------------
q_file = open("questions.txt", "r")
content = q_file.read()
original_question_list = content.split("\n")
question_set = set(original_question_list)
q_file.close()

# GAME STATUS CATEGORIES ------------------------------------------------------
STATUS_PLAYING = "playing"
STATUS_FINISHED = "done"

# DEFAULT MESSAGES ------------------------------------------------------------
START = "MAGIC HAT"
INTRO = "Magic hat is a game you can play with your team. \nPick a question out of the hat and learn more about your teammates!"
MOVE_QUERY = "\nDo you want to: \n1 - Get a question, \n2 - Turn on auto-ask, or \nQ - Quit?"
TIME_QUERY = "\nHow often would you like to receive a question? Enter # of seconds:"
TIME_ERROR = "Sorry, I didn't understand that. Enter # of seconds:"
AUTO_OFF = "\nTurned off auto-ask!"
ENDING = "\nHope you enjoyed the questions with your team! :)"
BAD_MOVE = "\nThe magic hat does not understand your request!"

# FUNCTIONS -------------------------------------------------------------------

def load_questions(filepath):
    """ Load questions from a text file."""

    q_file = open(filepath, "r")
    content = q_file.read()
    original_question_list = content.split("\n")
    question_set = set(question_list)
    q_file.close()

    return original_question_list, question_set


def show_hat():
    """ Displays a random hat image."""

    num = random.randint(0,(len(hats)-1))

    print(hats[num])


def retrieve_input():
    """ Get user input. """

    reply = input("> ").upper()

    return reply

# GAME CLASS ------------------------------------------------------------------

class Game(object):
    """ A Magic Hat Game object. (game.Game)

    Methods:
    start: Begin the game (bool)
    get_question: Get a unique question.
    all_asked_already: Check if all questions have been asked already (bool)
    reset_questions: Reset question set once all 200 questions have been asked.
    get_status: Get status of gameplay (bool)

    """

    def __init__(self):
        self.status = STATUS_PLAYING
        self.question_list = original_question_list.copy()
        self.asked_questions = set()    # already asked questions
        self.auto_ask = False           # periodic questions
        self.playing = True             # game in progress
        self.start_time = time.time()


    def start(self):
        """ Display the title and instructions of the game """

        # load_questions(filepath)
        print(START)
        show_hat()
        print(INTRO)

        return self.status


    def get_question(self):
        """ Randomly selects question from questions list.
        Display a new question that hasn't been asked yet.
        When all questions have been asked, reset the set."""

        if len(self.question_list) != 0:
            question = random.choice(self.question_list)
            self.question_list.remove(question)
            self.asked_questions.add(question)
        else:
            self.reset_questions()

        return question


    def all_asked_already(self):
        """ Return true if all questions have been asked already. """

        return question_set == self.asked_questions


    def reset_questions(self):
        """When all questions have been asked, reset the list."""

        self.question_list = original_question_list.copy()


    def get_status(self):
        """ Get the current status of gameplay. """

        return self.playing


# PLAY GAME FUNCTION ----------------------------------------------------------

def play_game():
    """ Initiate gameplay. """

    game = Game()
    game.start()

    while game.playing:
        print(MOVE_QUERY)
        choice = retrieve_input()

        # Get a question
        if choice == "1":
            print(game.get_question())

        # Turn on auto-ask
        elif choice == "2":
            print(TIME_QUERY)
            while True:
                try:
                    seconds = int(input("> "))
                except ValueError:
                    print(TIME_ERROR)
                    continue    # Try again... Return to the start of the loop.
                else:
                    break       # Seconds successfully parsed! Exiting the loop.
            print(f"Magic Hat will ask a question every {seconds} seconds. \nType 'S' to stop auto-asking questions.\n")
            game.auto_ask = True
            while game.auto_ask:
                print("\n",game.get_question())
                time.sleep(seconds)

                if keyboard.is_pressed("s"):
                    print(AUTO_OFF)
                    game.auto_ask = False
                    break
        # Quit
        elif choice == "Q":
            print(ENDING)
            game.playing = False
            game.status = STATUS_FINISHED
            return game.status

        else:
            print(BAD_MOVE)

# EXECUTE GAME ----------------------------------------------------------------

if __name__ == '__main__':
    play_game()
