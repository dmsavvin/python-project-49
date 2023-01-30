'''Configuration variables and task generating function for the even game'''
import random

_EVEN_RANGE = (1, 100)
'''Range of the values (both ends included) for the even game'''


def get_even_task():
    '''Return the task and the correct answer for the even game.

    Returns: a tuple (task_repr, correct_answer) where
        task_repr - a string with a task to be solved during
        the even game round
        correct_answer - a string to be compared with the answer
        provided by the player of the even game
    '''
    number = random.randint(*_EVEN_RANGE)
    task_repr = str(number)
    correct_answer = 'no' if number % 2 else 'yes'

    return task_repr, correct_answer
