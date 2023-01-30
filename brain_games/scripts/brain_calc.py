#!/usr/bin/env python3
'''This script starts calc game'''
from brain_games.games import GAMES
from brain_games.play_game import play_game


def main():
    play_game(*GAMES['calc'])


if __name__ == '__main__':
    main()
