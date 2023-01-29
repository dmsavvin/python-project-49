import prompt


def play_game(game_manual, problem_generator, number_of_rounds):

    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')

    print(game_manual)

    for _ in range(number_of_rounds):
        problem_representation, expected_answer = problem_generator()
        print(f'Question: {problem_representation}')
        given_answer = prompt.string('Your answer: ')
        if expected_answer != given_answer:
            print(f"'{given_answer}' is wrong answer ;(. "
                  f"Correct answer was '{expected_answer}'.")
            print(f"Let's try again, {player_name}!")
            break
        print('Correct!')
    else:
        print(f'Congratulations, {player_name}!')
