'''Configuration variables and task generating function for prime game'''
import random

_PRIME_RANGE = (1, 100)
'''Range of the values (both ends included) for the prime game'''


def _is_prime(num):
    '''Return True if num is prime False otherwise'''
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True


def get_prime_task():
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
