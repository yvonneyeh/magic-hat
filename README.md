# Magic Hat
Magic hat is a command line game you can play with your team, where you pick a question out of a hat, as a team-building exercise.

```
 __  __             _        _    _       _              /`_>
|  \/  |           (_)      | |  | |     | |           / /
| \  / | __ _  __ _ _  ___  | |__| | __ _| |_          |/
| |\/| |/ _` |/ _` | |/ __| |  __  |/ _` | __|     ____|    __
| |  | | (_| | (_| | | (__  | |  | | (_| | |_     |    \.-``  )
|_|  |_|\__,_|\__, |_|\___| |_|  |_|\__,_|\__|    |---``\  _.'
               __/ |                           .-`'---``_.'
              |___/                           (__...--``
```

## Gameplay

1. Clone this repository:
```shell
git clone https://github.com/yvonneyeh/magic-hat.git
```

***Optional***: Create and activate a virtual environment:
```shell
pip3 install virtualenv
virtualenv env
source env/bin/activate
```

2. Install dependencies:
```shell
pip3 install -r requirements.txt
```

3. To play, run the following in your terminal:
```shell
sudo python3 game.py
```

4. To execute tests:
```shell
python3 tests.py
```

## Features
- Users can ask the hat to give you a question.
- Ask the hat to ask questions every X seconds.
- Ask the hat to turn off the periodic questions
- The hat should not repeat questions that have been asked before (unless they've all been asked already)

#### Icebreaker Questions
- Examples of questions would be “what was your childhood nickname?” Or “what is your favorite emoji and why?”.
- All questions are from [this list of icebreaker questions](https://conversationstartersworld.com/icebreaker-questions/)

## Design

My original attempt to create this game is located in [`original.py`](https://github.com/yvonneyeh/magic-hat/blob/main/original.py), you can see that prior to refactoring, the code wasn't quite DRY and had some repetition in logic. I refactored the code to separate larger functions into smaller and more abstracted logic to reduce complexity and increase efficiency.

- By implementing a Game class, we can access class attributes that allow for more easily tested components.
- Sets were also used to speed up lookup time for previously asked questions.
- Python provides a library named `keyboard` which is used here to get full control of a user's keypresses.

#### Future Updates
- Keep track of time with Unix timestamp: `start_time` and `next_time`
- Refactor `play_game()` to use switch case instead of if/elif statements
