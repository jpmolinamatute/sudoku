#!/usr/bin/env python

from connection import Connection
from sudoku import Sudoku
from window import Example
from PyQt5.QtWidgets import QApplication
import sys


if __name__ == "__main__":
    try:
        db = Connection('localhost', '27017', 'sudoku', 'sud', 'vzla')
        sud = Sudoku()
        grid = db.getGrid()
        if grid is None:
            sud.createSudoku()
            grid = sud.getSudoku()
            db.insertGrid(grid)
        else:
            sud.setSudoku(grid)

        # print(sud)
        app = QApplication(sys.argv)
        ex = Example(grid)
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        print("Stopped by Keysstroke")
        exit(1)
    except Exception as e:
        print(e)
        exit(1)
