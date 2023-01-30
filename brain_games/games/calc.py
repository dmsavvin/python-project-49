'''Configuration variables and task generating function for the calc game'''
import random

_CALC_RANGE = (1, 50)
_CALC_OPERATIONS = ('+', '-', '*', '//', '**')
'''Range of the values (both ends included) and set of operators
for the calc game
'''


def get_calc_task():
    '''Return the task and the correct answer for the calc game.

    Returns: a tuple (task_repr, correct_answer) where
        task_repr - a string with a task to be solved during
        the calc game round
        correct_answer - a string to be compared with the answer
        provided by the player of the calc game
    '''
    first_number = random.randint(*_CALC_RANGE)
    second_number = random.randint(*_CALC_RANGE)
    operator = random.choice(_CALC_OPERATIONS)
    task_repr = f'{first_number} {operator} {second_number}'
    correct_answer = str(eval(task_repr))

    return task_repr, correct_answer
