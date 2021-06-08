# Magic Hat
Magic hat is a command line game you can play with your team, where you pick a question out of a hat, as a team-building exercise.

## Gameplay

To play, run the following in your terminal:
```
python3 game.py
```

To execute tests:
```
python3 tests.py
```

## Features
- Users can ask the hat to give you a question.
- Ask the hat to ask questions every X seconds.
- Ask the hat to turn off the periodic questions
- The hat should not repeat questions that have been asked before (unless they've all been asked already)

#### Icebreaker Questions:
- Examples of questions would be “what was your childhood nickname?” Or “what is your favorite emoji and why?”.
- All questions are from [this list of icebreaker questions](https://conversationstartersworld.com/icebreaker-questions/)

## Design

My original attempt to create this game is located in [`original.py`](https://github.com/yvonneyeh/magic-hat/blob/main/original.py), you can see that prior to refactoring, the code wasn't quite DRY and had some repitition in logic. I refactored the code to separate larger functions into smaller and more abstracted logic to reduce complexity and increase efficiency. By implementing a Game class, we can access class attributes that allow for more easily tested components.
