from brain_games import problem_generators

_MANUALS = {'gcd': "Find the greatest common divisor of given numbers.",
            'calc': "What is the result of the expression?",
            'even': "Answer 'yes' if number even otherwise answer 'no'.",
            'prime': "Answer 'yes' if given number is prime. Otherwise \
                      answer 'no'.",
            'prog': "What number is missing in this progression?"
            }

_GENERATORS = {'gcd': problem_generators.gcd_problem_generator,
               'calc': problem_generators.calc_problem_generator,
               'even': problem_generators.even_problem_generator,
               'prime': problem_generators.prime_problem_generator,
               'prog': problem_generators.progression_problem_generator
               }

# Each game is described as a list of the following items:
# [0] manual string explaining game rules
# [1] problem generator function returning the problem
#     representation and the expected answer
# [2] number of rounds in the game
GAMES = {'gcd': [_MANUALS['gcd'], _GENERATORS['gcd'], 3],
         'calc': [_MANUALS['calc'], _GENERATORS['calc'], 3],
         'even': [_MANUALS['even'], _GENERATORS['even'], 3],
         'prime': [_MANUALS['prime'], _GENERATORS['prime'], 3],
         'prog': [_MANUALS['prog'], _GENERATORS['prog'], 3]
         }
