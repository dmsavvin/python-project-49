import prompt


def play(game_manual, task_generator, number_of_rounds):
    '''Implement the logic for the game specified with arguments

    Args:
        game_manual (str): game rules description
        task_generator (func): function generating the task and
           the correct answer for each round of the game
        number_of_rounds (int): maximum number of rounds to be
            played in the game
    '''
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')

    print(game_manual)

    for _ in range(number_of_rounds):

        task_repr, correct_answer = task_generator()

        print(f'Question: {task_repr}')
        given_answer = prompt.string('Your answer: ')

        if correct_answer != given_answer:
            print(f"'{given_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {player_name}!")
            break

        print('Correct!')

    else:
        print(f'Congratulations, {player_name}!')
