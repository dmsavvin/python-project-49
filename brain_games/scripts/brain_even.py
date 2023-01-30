#!/usr/bin/env python3
'''This script starts even game'''
from brain_games.games.game_dir import GAMES
from brain_games.games.play import play


def main():
    play(*GAMES['even'])


if __name__ == '__main__':
    main()
