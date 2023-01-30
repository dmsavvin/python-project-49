'''Functions of this module generate the task and the answer for each game

Each function returns a tuple (task_repr, correct_answer) where task_repr
is a string representing the task to be solved by the player and correct_answer
is a string representing the correct answer for the task from the task_repr
'''
import math
import random

_GCD_RANGE = (1, 100)
'''Range of the values (both ends included) for the gcd game'''

_CALC_RANGE = (1, 100)
_CALC_OPERATIONS = ('+', '-', '*', '//', '**')
'''Range of the values (both ends included) and set of operators
for the calc game
'''

_EVEN_RANGE = (1, 100)
'''Range of the values (both ends included) for the even game'''

_PRIME_RANGE = (1, 100)
'''Range of the values (both ends included) for the prime game'''

_PROG_START_RANGE = (1, 10)
_PROG_STEP_RANGE = (1, 9)
_PROG_LEN_RANGE = (5, 15)
'''Range of values (both ends included) for the initial term, common
difference and the length of the arithmetic progression for the
progression game
'''


def gcd_task_generator():
    '''Return the task and the correct answer for the gcd game.

    Returns: a tuple (task_repr, correct_answer) where
        task_repr - a string with a task to be solved during
        the gcd game round
        correct_answer - a string to be compared with the answer
        provided by the player of the gcd game
    '''
    first_number = random.randint(*_GCD_RANGE)
    second_number = random.randint(*_GCD_RANGE)
    task_repr = f'{first_number}, {second_number}'
    correct_answer = str(math.gcd(first_number, second_number))

    return task_repr, correct_answer


def calc_task_generator():
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


def even_task_generator():
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


def _is_prime(num):
    '''Return True if num is prime False otherwise'''
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True


def prime_task_generator():
    '''Return the task and the correct answer for the prime game.

    Returns: a tuple (task_repr, correct_answer) where
        task_repr - a string with a task to be solved during
        the prime game round
        correct_answer - a string to be compared with the answer
        provided by the player of the prime game
    '''
    number = random.randint(*_PRIME_RANGE)
    task_repr = str(number)
    correct_answer = 'yes' if _is_prime(number) else 'no'

    return task_repr, correct_answer


def prog_task_generator():
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

    prog = [prog_start + prog_step * _ for _ in range(prog_len)]
    screened_pos = random.randrange(prog_len)
    task_repr = ' '.join(['..' if index == screened_pos else str(value)
                         for index, value in enumerate(prog)])
    correct_answer = str(prog[screened_pos])

    return task_repr, correct_answer
