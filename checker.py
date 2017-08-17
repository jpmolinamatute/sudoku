#!/usr/bin/env python

from sys import exit
from pymongo import MongoClient


class SudokuGUI:
    db = None

    def __init__(self, host, port, user, password, db):
        if user and password:
            mongoURL = "mongodb://" + user + ":" + password + "@"
        else:
            mongoURL = "mongodb://"
        mongoURL += host + ":" + port + "/" + db
        self.db = MongoClient(mongoURL)[db]

    def checkSudoku(self, sudoku):
        if isinstance(sudoku, dict) and len(sudoku) == 81:
            for section in range(1, 10):
                sec = "s" + str(section)
                for position in range(1, 10):
                    pos = sec + "p" + str(position)
                    if type(sudoku[pos]) != int or sudoku[pos] < 0 or sudoku[pos] > 9:
                        raise ValueError("Position " + pos + " is wrong!")
        else:
            raise ValueError("Invalid sudoku length")

    def insertSudoku(self, sudoku):
        self.checkSudoku(sudoku)
        result = self.db.sudoku.insert_one(sudoku)
        print("New sudoku was added successfully")
        print("Id: ", result.inserted_id)

    def printCollection(self):
        cursor = self.db.pre_build_dashboards.find()
        for document in cursor:
            print(document)


def startPoint():
    try:
        sudoku = SudokuGUI("localhost", "27017",
                           "tester", "test", "webui-test")
        sudoku.insertSudoku({
            "s1p1": 0,
            "s1p2": 0,
            "s1p3": 0,
            "s1p4": 0,
            "s1p5": 0,
            "s1p6": 0,
            "s1p7": 0,
            "s1p8": 0,
            "s1p9": 0,
            "s2p1": 0,
            "s2p2": 0,
            "s2p3": 0,
            "s2p4": 0,
            "s2p5": 0,
            "s2p6": 0,
            "s2p7": 0,
            "s2p8": 0,
            "s2p9": 0,
            "s3p1": 0,
            "s3p2": 0,
            "s3p3": 0,
            "s3p4": 0,
            "s3p5": 0,
            "s3p6": 0,
            "s3p7": 0,
            "s3p8": 0,
            "s3p9": 0,
            "s4p1": 0,
            "s4p2": 0,
            "s4p3": 0,
            "s4p4": 0,
            "s4p5": 0,
            "s4p6": 0,
            "s4p7": 0,
            "s4p8": 0,
            "s4p9": 0,
            "s5p1": 0,
            "s5p2": 9,
            "s5p3": 9,
            "s5p4": 0,
            "s5p5": 0,
            "s5p6": 0,
            "s5p7": 0,
            "s5p8": 0,
            "s5p9": 0,
            "s6p1": 0,
            "s6p2": 0,
            "s6p3": 0,
            "s6p4": 0,
            "s6p5": 0,
            "s6p6": 0,
            "s6p7": 0,
            "s6p8": 0,
            "s6p9": 0,
            "s7p1": 0,
            "s7p2": 0,
            "s7p3": 0,
            "s7p4": 0,
            "s7p5": 0,
            "s7p6": 0,
            "s7p7": 0,
            "s7p8": 0,
            "s7p9": 0,
            "s8p1": 0,
            "s8p2": 0,
            "s8p3": 0,
            "s8p4": 0,
            "s8p5": 0,
            "s8p6": 0,
            "s8p7": 0,
            "s8p8": 0,
            "s8p9": 0,
            "s9p1": 0,
            "s9p2": 0,
            "s9p3": 0,
            "s9p4": 0,
            "s9p5": 0,
            "s9p6": 0,
            "s9p7": 0,
            "s9p8": 0,
            "s9p9": 0
        })
        # sudoku.printCollection()
        exit(0)
    except KeyboardInterrupt:
        exit(1)
    except ValueError as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    startPoint()
