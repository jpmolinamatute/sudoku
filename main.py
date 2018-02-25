#!/usr/bin/env python

from connection import Connection
from sudoku import Sudoku


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
            print(myMain.sud)
        else:
            myMain.printCollection(grid)
        exit(0)
    except KeyboardInterrupt:
        print("Stopped by Keysstroke")
        exit(1)
    except Exception as e:
        print(e)
        exit(1)
