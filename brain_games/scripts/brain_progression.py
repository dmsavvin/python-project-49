from brain_games.games import GAMES
from brain_games.play_game import play_game


def main():
    play_game(*GAMES['prog'])


if __name__ == '__main__':
    main()
