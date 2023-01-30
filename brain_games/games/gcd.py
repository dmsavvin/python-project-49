'''Configuration variables and task generating function for gcd game'''
import math
import random

_GCD_RANGE = (1, 100)
'''Range of the values (both ends included) for the gcd game'''


def get_gcd_task():
    '''Return the task and the correct answer for the gcd game.

    Returns: a tuple (task_repr, correct_answer) where
        task_repr - a string with a task to be solved during
        the gcd game round
        correct_answer - a string to be compared with the answer
        provided by the player of the gcd game
    '''
    first_number = random.randint(*_GCD_RANGE)
    second_number = random.randint(*_GCD_RANGE)
    task_repr = f'{first_number} {second_number}'
    correct_answer = str(math.gcd(first_number, second_number))

    return task_repr, correct_answer
