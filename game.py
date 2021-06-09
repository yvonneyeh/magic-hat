import sys
import random
import time
from hats import hats
import keyboard


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
    new_question: Get a unique question.
    reset_questions: Reset question set once all 200 questions have been asked.
    get_status: Get status of gameplay (bool)

    """

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
        print(MOVE_QUERY)
        choice = input("> ").upper()

        if choice == "1":
            print(game.new_question())
            # print("set:", game.asked_Qs)

        elif choice == "2":
            print(TIME_QUERY)
            # seconds = int(input("> "))
            while True:
                try:
                    seconds = int(input("> "))
                except ValueError:
                    print("Sorry, I didn't understand that. Enter # of seconds:")
                    # Try again... Return to the start of the loop
                    continue
                else:
                    # Seconds successfully parsed! Exiting the loop.
                    break
            print(f"Magic Hat will ask a question every {seconds} seconds. \nType 'S' to stop auto-asking questions.\n")
            game.auto_ask = True
            while game.auto_ask:
                print(game.new_question())
                time.sleep(seconds)

                # if keyboard.wait("s"):
                # keyboard.on_press_key("s", lambda _:print('Turned off auto-ask!'))
                if keyboard.is_pressed("s"):
                # if keyboard.read_key() == "s":
                    print(AUTO_OFF)
                    game.auto_ask = False
                    break


                # try:  # used try so that if user pressed other than the given key error will not be shown
                #     if keyboard.is_pressed('S'):  # if key 's' is pressed
                #         print('Turned off auto-ask!')
                #         break  # finishing the loop
                # except:
                #     break  # if user pressed a key other than the given key the loop will break
                # user_input = input()
                # if user_input.upper() == "S":
                #     game.auto_ask = False
                #     break

        elif choice == "Q":
            print(ENDING)
            game.playing = False
            game.status = STATUS_FINISHED
            return game.status

        else:
            print(BAD_MOVE)


if __name__ == '__main__':
    # print(question_set)
    play_game()

    # ticktock()

    # game = Game()
    # print(game.asked_Qs)
    # game.new_question()
