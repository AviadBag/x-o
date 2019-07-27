from Board import Board
from Player import Player


def main():
    player1 = Player("X", 'שחקן א')
    player2 = Player("O", 'שחקן ב')
    board = Board(player1, player2)

    board.show()


if __name__ == '__main__':
    main()
