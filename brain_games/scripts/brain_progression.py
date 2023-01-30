#!/usr/bin/env python3
'''This script starts progression game'''
from brain_games.games.game_dir import GAMES
from brain_games.games.play import play


def main():
    play(*GAMES['prog'])


if __name__ == '__main__':
    main()
