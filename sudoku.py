#!/usr/bin/env python

import itertools
import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def attempt_board(m=3):
    """Make one attempt to generate a filled m**2 x m**2 Sudoku board, returning the board if successful, or None if not.
    https://codereview.stackexchange.com/questions/88849/sudoku-puzzle-generator
    """
    n = m**2

    numbers = list(range(1, n + 1))
    board = [[None for _ in range(n)] for _ in range(n)]
    for i, j in itertools.product(range(n), repeat=2):
        i0, j0 = i - i % m, j - j % m  # origin of mxm block

        random.shuffle(numbers)
        # row (x not in board[i]
        # column all(row[j] != x for row in board)
        # block all(x not in row[j0:j0 + m]
        for x in numbers:
            if (x not in board[i] and
                all(row[j] != x for row in board) and
                all(x not in row[j0:j0 + m]
                    for row in board[i0:i])):
                board[i][j] = x
                break
        else:
            # No number is valid in this cell.
            return None
    return board


class Sudoku:
    grid = {}

    def __str__(self):
        return str(self.grid["S1P1"]) + " " + str(self.grid["S1P2"]) + " " + str(self.grid["S1P3"]) + " |  " + \
            str(self.grid["S2P1"]) + " " + str(self.grid["S2P2"]) + " " + str(self.grid["S2P3"]) + " |  " +\
            str(self.grid["S3P1"]) + " " + str(self.grid["S3P2"]) + " " + str(self.grid["S3P3"]) + "\n" +\
            str(self.grid["S1P4"]) + " " + str(self.grid["S1P5"]) + " " + str(self.grid["S1P6"]) + " |  " +\
            str(self.grid["S2P4"]) + " " + str(self.grid["S2P5"]) + " " + str(self.grid["S2P6"]) + " |  " +\
            str(self.grid["S3P4"]) + " " + str(self.grid["S3P5"]) + " " + str(self.grid["S3P6"]) + "\n" +\
            str(self.grid["S1P7"]) + " " + str(self.grid["S1P8"]) + " " + str(self.grid["S1P9"]) + " |  " +\
            str(self.grid["S2P7"]) + " " + str(self.grid["S2P8"]) + " " + str(self.grid["S2P9"]) + " |  " +\
            str(self.grid["S3P7"]) + " " + str(self.grid["S3P8"]) + " " + str(self.grid["S3P9"]) + "\n" +\
            "-----------------------\n" +\
            str(self.grid["S4P1"]) + " " + str(self.grid["S4P2"]) + " " + str(self.grid["S4P3"]) + " |  " +\
            str(self.grid["S5P1"]) + " " + str(self.grid["S5P2"]) + " " + str(self.grid["S5P3"]) + " |  " +\
            str(self.grid["S6P1"]) + " " + str(self.grid["S6P2"]) + " " + str(self.grid["S6P3"]) + "\n" +\
            str(self.grid["S4P4"]) + " " + str(self.grid["S4P5"]) + " " + str(self.grid["S4P6"]) + " |  " +\
            str(self.grid["S5P4"]) + " " + str(self.grid["S5P5"]) + " " + str(self.grid["S5P6"]) + " |  " +\
            str(self.grid["S6P4"]) + " " + str(self.grid["S6P5"]) + " " + str(self.grid["S6P6"]) + "\n" +\
            str(self.grid["S4P7"]) + " " + str(self.grid["S4P8"]) + " " + str(self.grid["S4P9"]) + " |  " +\
            str(self.grid["S5P7"]) + " " + str(self.grid["S5P8"]) + " " + str(self.grid["S5P9"]) + " |  " +\
            str(self.grid["S6P7"]) + " " + str(self.grid["S6P8"]) + " " + str(self.grid["S6P9"]) + "\n" +\
            "-----------------------\n" +\
            str(self.grid["S7P1"]) + " " + str(self.grid["S7P2"]) + " " + str(self.grid["S7P3"]) + " |  " +\
            str(self.grid["S8P1"]) + " " + str(self.grid["S8P2"]) + " " + str(self.grid["S8P3"]) + " |  " +\
            str(self.grid["S9P1"]) + " " + str(self.grid["S9P2"]) + " " + str(self.grid["S9P3"]) + "\n" +\
            str(self.grid["S7P4"]) + " " + str(self.grid["S7P5"]) + " " + str(self.grid["S7P6"]) + " |  " +\
            str(self.grid["S8P4"]) + " " + str(self.grid["S8P5"]) + " " + str(self.grid["S8P6"]) + " |  " +\
            str(self.grid["S9P4"]) + " " + str(self.grid["S9P5"]) + " " + str(self.grid["S9P6"]) + "\n" +\
            str(self.grid["S7P7"]) + " " + str(self.grid["S7P8"]) + " " + str(self.grid["S7P9"]) + " |  " +\
            str(self.grid["S8P7"]) + " " + str(self.grid["S8P8"]) + " " + str(self.grid["S8P9"]) + " |  " + \
            str(self.grid["S9P7"]) + " " + str(self.grid["S9P8"]
                                               ) + " " + str(self.grid["S9P9"]) + "\n"

    def setSudoku(self, board):
        if isinstance(board, dict):
            if len(board) == 81:
                for i, j in itertools.product(range(9), repeat=2):
                    index = "S" + str(i + 1) + "P" + str(j + 1)
                    if not isinstance(board[index], int):
                        raise Exception("Invalid board")
                self.grid = board
            else:
                raise Exception("Invalid sudoku length")
        else:
            raise Exception("Invalid sudoku format")

    def createSudoku(self):
        board = None
        while board is None:
            board = attempt_board()
        self.grid["S1P1"] = board[0][0]
        self.grid["S1P2"] = board[0][1]
        self.grid["S1P3"] = board[0][2]
        self.grid["S1P4"] = board[1][0]
        self.grid["S1P5"] = board[1][1]
        self.grid["S1P6"] = board[1][2]
        self.grid["S1P7"] = board[2][0]
        self.grid["S1P8"] = board[2][1]
        self.grid["S1P9"] = board[2][2]
        self.grid["S2P1"] = board[0][3]
        self.grid["S2P2"] = board[0][4]
        self.grid["S2P3"] = board[0][5]
        self.grid["S2P4"] = board[1][3]
        self.grid["S2P5"] = board[1][4]
        self.grid["S2P6"] = board[1][5]
        self.grid["S2P7"] = board[2][3]
        self.grid["S2P8"] = board[2][4]
        self.grid["S2P9"] = board[2][5]
        self.grid["S3P1"] = board[0][6]
        self.grid["S3P2"] = board[0][7]
        self.grid["S3P3"] = board[0][8]
        self.grid["S3P4"] = board[1][6]
        self.grid["S3P5"] = board[1][7]
        self.grid["S3P6"] = board[1][8]
        self.grid["S3P7"] = board[2][6]
        self.grid["S3P8"] = board[2][7]
        self.grid["S3P9"] = board[2][8]
        self.grid["S4P1"] = board[3][0]
        self.grid["S4P2"] = board[3][1]
        self.grid["S4P3"] = board[3][2]
        self.grid["S4P4"] = board[4][0]
        self.grid["S4P5"] = board[4][1]
        self.grid["S4P6"] = board[4][2]
        self.grid["S4P7"] = board[5][0]
        self.grid["S4P8"] = board[5][1]
        self.grid["S4P9"] = board[5][2]
        self.grid["S5P1"] = board[3][3]
        self.grid["S5P2"] = board[3][4]
        self.grid["S5P3"] = board[3][5]
        self.grid["S5P4"] = board[4][3]
        self.grid["S5P5"] = board[4][4]
        self.grid["S5P6"] = board[4][5]
        self.grid["S5P7"] = board[5][3]
        self.grid["S5P8"] = board[5][4]
        self.grid["S5P9"] = board[5][5]
        self.grid["S6P1"] = board[3][6]
        self.grid["S6P2"] = board[3][7]
        self.grid["S6P3"] = board[3][8]
        self.grid["S6P4"] = board[4][6]
        self.grid["S6P5"] = board[4][7]
        self.grid["S6P6"] = board[4][8]
        self.grid["S6P7"] = board[5][6]
        self.grid["S6P8"] = board[5][7]
        self.grid["S6P9"] = board[5][8]
        self.grid["S7P1"] = board[6][0]
        self.grid["S7P2"] = board[6][1]
        self.grid["S7P3"] = board[6][2]
        self.grid["S7P4"] = board[7][0]
        self.grid["S7P5"] = board[7][1]
        self.grid["S7P6"] = board[7][2]
        self.grid["S7P7"] = board[8][0]
        self.grid["S7P8"] = board[8][1]
        self.grid["S7P9"] = board[8][2]
        self.grid["S8P1"] = board[6][3]
        self.grid["S8P2"] = board[6][4]
        self.grid["S8P3"] = board[6][5]
        self.grid["S8P4"] = board[7][3]
        self.grid["S8P5"] = board[7][4]
        self.grid["S8P6"] = board[7][5]
        self.grid["S8P7"] = board[8][3]
        self.grid["S8P8"] = board[8][4]
        self.grid["S8P9"] = board[8][5]
        self.grid["S9P1"] = board[6][6]
        self.grid["S9P2"] = board[6][7]
        self.grid["S9P3"] = board[6][8]
        self.grid["S9P4"] = board[7][6]
        self.grid["S9P5"] = board[7][7]
        self.grid["S9P6"] = board[7][8]
        self.grid["S9P7"] = board[8][6]
        self.grid["S9P8"] = board[8][7]
        self.grid["S9P9"] = board[8][8]

    def getSudoku(self):
        return self.grid
