'''This module provides description for each game

Each game description is a tuple of three elements: [0] manual string explaining
game rules, [1] task generator function returning the task representation and
the correct answer [2] maximum number of rounds in the game
'''
from brain_games import task_generators

_MANUALS = {'gcd': "Find the greatest common divisor of given numbers.",
            'calc': "What is the result of the expression?",
            'even': "Answer 'yes' if number even otherwise answer 'no'.",
            'prime': ("Answer 'yes' if given number is prime. Otherwise "
                      "answer 'no'."),
            'prog': "What number is missing in this progression?"
            }
'''Manuals for the games'''

_GENERATORS = {'gcd': task_generators.gcd_task_generator,
               'calc': task_generators.calc_task_generator,
               'even': task_generators.even_task_generator,
               'prime': task_generators.prime_task_generator,
               'prog': task_generators.prog_task_generator
               }
'''Task generator functions for the games'''

_NUMBER_OF_ROUNDS = 3
'''Maximum number of rounds for the games'''

GAMES = {'gcd': (_MANUALS['gcd'], _GENERATORS['gcd'], _NUMBER_OF_ROUNDS),
         'calc': (_MANUALS['calc'], _GENERATORS['calc'], _NUMBER_OF_ROUNDS),
         'even': (_MANUALS['even'], _GENERATORS['even'], _NUMBER_OF_ROUNDS),
         'prime': (_MANUALS['prime'], _GENERATORS['prime'], _NUMBER_OF_ROUNDS),
         'prog': (_MANUALS['prog'], _GENERATORS['prog'], _NUMBER_OF_ROUNDS)
         }
'''Descriptions for the games.

Each game description is a tuple of three elements: [0] manual string explaining
game rules, [1] task generator function returning the task representation and
the correct answer [2] maximum number of rounds in the game
'''
