'''Configuration variable and task generating function for progression game'''
import random

_PROG_START_RANGE = (1, 10)
_PROG_STEP_RANGE = (1, 9)
_PROG_LEN_RANGE = (5, 15)
'''Range of values (both ends included) for the initial term, common
difference and the length of the arithmetic progression for the
progression game
'''


def get_prog_task():
    '''Return the task and the correct answer for the progression game.

    Returns: a tuple (task_repr, correct_answer) where
        task_repr - a string with a task to be solved during
        the progression game round
        correct_answer - a string to be compared with the answer
        provided by the player of the progression game
    '''
    prog_start = random.randint(*_PROG_START_RANGE)
    prog_step = random.randint(*_PROG_STEP_RANGE)
    prog_len = random.randint(*_PROG_LEN_RANGE)
    screened_pos = random.randrange(prog_len)

    prog = [prog_start + prog_step * _ for _ in range(prog_len)]
    task_repr = ' '.join(['..' if index == screened_pos else str(value)
                         for index, value in enumerate(prog)])
    correct_answer = str(prog[screened_pos])

    return task_repr, correct_answer
