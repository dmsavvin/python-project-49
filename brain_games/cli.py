#!/usr/bin/env python3


import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')


if __name__ == '__main__':
    print('I am in cli.py')
    welcome_user()
