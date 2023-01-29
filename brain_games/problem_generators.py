import math
import random


def gcd_problem_generator():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    problem_representation = f'{first_number}, {second_number}'
    expected_answer = str(math.gcd(first_number, second_number))

    return problem_representation, expected_answer


def calc_problem_generator():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    operator = random.choice(('+', '-', '*', '//', '**'))
    problem_representation = f'{first_number} {operator} {second_number}'
    expected_answer = str(eval(problem_representation))

    return problem_representation, expected_answer


def even_problem_generator():
    number = random.randint(1, 100)
    problem_representation = str(number)
    expected_answer = 'no' if number % 2 else 'yes'

    return problem_representation, expected_answer


def prime_problem_generator():

    def is_prime(num):
        for n in range(2, int(num ** 0.5) + 1):
            if num % n == 0:
                return False
        return True

    number = random.randint(1, 100)
    problem_representation = str(number)
    expected_answer = 'yes' if is_prime(number) else 'no'

    return problem_representation, expected_answer


def progression_problem_generator():

    pass
