#!/usr/bin/env python
from sys import exit
from random import randrange


class Sudoku:
    grid = {}
    posibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    mapByRow = [
        ["s1p1", "s1p2", "s1p3", "s2p1", "s2p2", "s2p3", "s3p1", "s3p2", "s3p3"],
        ["s1p4", "s1p5", "s1p6", "s2p4", "s2p5", "s2p6", "s3p4", "s3p5", "s3p6"],
        ["s1p7", "s1p8", "s1p9", "s2p7", "s2p8", "s2p9", "s3p7", "s3p8", "s3p9"],
        ["s4p1", "s4p2", "s4p3", "s5p1", "s5p2", "s5p3", "s6p1", "s6p2", "s6p3"],
        ["s4p4", "s4p5", "s4p6", "s5p4", "s5p5", "s5p6", "s6p4", "s6p5", "s6p6"],
        ["s4p7", "s4p8", "s4p9", "s5p7", "s5p8", "s5p9", "s6p7", "s6p8", "s6p9"],
        ["s7p1", "s7p2", "s7p3", "s8p1", "s8p2", "s8p3", "s9p1", "s9p2", "s9p3"],
        ["s7p4", "s7p5", "s7p6", "s8p4", "s8p5", "s8p6", "s9p4", "s9p5", "s9p6"],
        ["s7p7", "s7p8", "s7p9", "s8p7", "s8p8", "s8p9", "s9p7", "s9p8", "s9p9"]
    ]

    mapByCol = [
        ["s1p1", "s1p4", "s1p7", "s4p1", "s4p4", "s4p7", "s7p1", "s7p4", "s7p7"],
        ["s1p2", "s1p5", "s1p8", "s4p2", "s4p5", "s4p8", "s7p2", "s7p5", "s7p8"],
        ["s1p3", "s1p6", "s1p9", "s4p3", "s4p6", "s4p9", "s7p3", "s7p6", "s7p9"],
        ["s2p1", "s2p4", "s2p7", "s5p1", "s5p4", "s5p7", "s8p1", "s8p4", "s8p7"],
        ["s2p2", "s2p5", "s2p8", "s5p2", "s5p5", "s5p8", "s8p2", "s8p5", "s8p8"],
        ["s2p3", "s2p6", "s2p9", "s5p3", "s5p6", "s5p9", "s8p3", "s8p6", "s8p9"],
        ["s3p1", "s3p4", "s3p7", "s6p1", "s6p4", "s6p7", "s9p1", "s9p4", "s9p7"],
        ["s3p2", "s3p5", "s3p8", "s6p2", "s6p5", "s6p8", "s9p2", "s9p5", "s9p8"],
        ["s3p3", "s3p6", "s3p9", "s6p3", "s6p6", "s6p9", "s9p3", "s9p6", "s9p9"]
    ]

    def __init__(self):
        self.clearTable()

    def getNumber(self):
        max = len(self.posibleValues)
        num = None
        if max == 1:
            num = self.posibleValues[0]
        elif max > 1:
            num = self.posibleValues[randrange(0, max)]

        if num is not None:
            self.posibleValues.remove(num)

        return num

    def printGrid(self):
        for section in range(0, 9):
            for position in range(0, 9):
                index = self.mapByRow[section][position]
                print(" " + str(self.grid[index]), end="")
                if position == 2 or position == 5:
                    print("  ", end="")
            print("")
            if section == 2 or section == 5:
                print(" ")

    def clearTable(self):
        for section in range(1, 10):
            sec = "s" + str(section)
            for position in range(1, 10):
                pos = sec + "p" + str(position)
                self.grid[pos] = 0

    def runChecks(self, myList, value):
        valid = True
        for l in myList:
            if self.grid[l] == value:
                valid = False

        return valid

    def checkSection(self, point, value):
        section = point[0:2]
        myList = [section + "p1", section + "p2", section + "p3", section + "p4", section +
                  "p5", section + "p6", section + "p7", section + "p8", section + "p9"]
        return self.runChecks(myList, value)

    def checkRow(self, point, value):
        for section in range(0, 9):
            for position in range(0, 9):
                if self.mapByRow[section][position] == point:
                    myList = self.mapByRow[section]
        return self.runChecks(myList, value)

    def checkCol(self, point, value):
        for section in range(0, 9):
            for position in range(0, 9):
                if self.mapByCol[section][position] == point:
                    myList = self.mapByCol[section]
        return self.runChecks(myList, value)

    def checkRules(self, point, value):
        section = self.checkSection(point, value)
        row = self.checkRow(point, value)
        col = self.checkCol(point, value)
        return col and row and section

    def navigate(self):
        restart = True
        while restart:
            breakForLoop = False
            for point in self.grid:
                valid = True
                while valid:
                    randNumber = self.getNumber()
                    if randNumber is None:
                        valid = False
                        breakForLoop = True
                    elif self.checkRules(point, randNumber):
                        self.grid[point] = randNumber
                        self.posibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                        valid = False
                        if point == "s9p9":
                            breakForLoop = True
                            restart = False
                if breakForLoop:
                    break


def startPoint():
    try:
        sudoku = Sudoku()
        # sudoku.navigate()
        # sudoku.printGrid()
        exit(0)
    except KeyboardInterrupt:
        print("", flush=True)
        sudoku.printGrid()
        exit(1)


if __name__ == "__main__":
    startPoint()
