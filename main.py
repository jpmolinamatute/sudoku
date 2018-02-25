#!/usr/bin/env python

from connection import Connection
from sudoku import Sudoku
from window import Example
from PyQt5.QtWidgets import QApplication
import sys


class Main:
    db = Connection('localhost', '27017', 'sudoku', 'sud', 'vzla')
    sud = Sudoku()

    def createSudoku(self):
        return self.sud.createSudoku()

    def printCollection(self, grid):
        self.sud.setSudoku(grid)
        print(self.sud)


if __name__ == "__main__":
    try:
        myMain = Main()
        grid = myMain.db.getGrid()
        if grid is None:
            myMain.createSudoku()
            myMain.db.insertGrid(myMain.sud.getSudoku())
            # print(myMain.sud)
        else:
            myMain.sud.setSudoku(grid)
            # myMain.printCollection(grid)

        app = QApplication(sys.argv)
        ex = Example(myMain.sud.getSudoku())
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        print("Stopped by Keysstroke")
        exit(1)
    except Exception as e:
        print(e)
        exit(1)
