'''Module provides description for each game'''
from brain_games.games import calc, even, gcd, prime, prog

_MANUALS = {'gcd': "Find the greatest common divisor of given numbers.",
            'calc': "What is the result of the expression?",
            'even': 'Answer "yes" if number even, otherwise answer "no".',
            'prime': ('Answer "yes" if given number is prime. Otherwise '
                      'answer "no".'),
            'prog': "What number is missing in this progression?"
            }
'''Manuals for the games'''

_GENERATORS = {'gcd': gcd.get_gcd_task,
               'calc': calc.get_calc_task,
               'even': even.get_even_task,
               'prime': prime.get_prime_task,
               'prog': prog.get_prog_task
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
