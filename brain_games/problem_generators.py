import math
import random

_GCD_RANGE = (1, 100)

_CALC_RANGE = (1, 100)
_CALC_OPERATIONS = ('+', '-', '*', '//', '**')

_EVEN_RANGE = (1, 100)

_PRIME_RANGE = (1, 100)

_PROG_START_RANGE = (1, 10)
_PROG_STEP_RANGE = (1, 9)
_PROG_LEN_RANGE = (5, 15)


def gcd_problem_generator():
    first_number = random.randint(*_GCD_RANGE)
    second_number = random.randint(*_GCD_RANGE)
    problem_repr = f'{first_number}, {second_number}'
    expected_answer = str(math.gcd(first_number, second_number))

    return problem_repr, expected_answer


def calc_problem_generator():
    first_number = random.randint(*_CALC_RANGE)
    second_number = random.randint(*_CALC_RANGE)
    operator = random.choice(_CALC_OPERATIONS)
    problem_repr = f'{first_number} {operator} {second_number}'
    expected_answer = str(eval(problem_repr))

    return problem_repr, expected_answer


def even_problem_generator():
    number = random.randint(*_EVEN_RANGE)
    problem_repr = str(number)
    expected_answer = 'no' if number % 2 else 'yes'

    return problem_repr, expected_answer


def prime_problem_generator():

    def is_prime(num):
        for n in range(2, int(num ** 0.5) + 1):
            if num % n == 0:
                return False
        return True

    number = random.randint(*_PRIME_RANGE)
    problem_repr = str(number)
    expected_answer = 'yes' if is_prime(number) else 'no'

    return problem_repr, expected_answer


def prog_problem_generator():

    prog_start = random.randint(*_PROG_START_RANGE)
    prog_step = random.randint(*_PROG_STEP_RANGE)
    prog_len = random.randint(*_PROG_LEN_RANGE)

    prog = [prog_start + prog_step * _ for _ in range(prog_len)]
    screened_pos = random.randrange(prog_len)
    problem_repr = ' '.join(['..' if index == screened_pos else str(value)
                            for index, value in enumerate(prog)])
    expected_answer = str(prog[screened_pos])

    return problem_repr, expected_answer
