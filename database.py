#!/usr/bin/env python

from sys import exit
from pymongo import MongoClient
from sudoku import Sudoku


class DataBase:
    db = None

    def __init__(self, host, port, user, password, db):
        if user and password:
            mongoURL = "mongodb://" + user + ":" + password + "@"
        else:
            mongoURL = "mongodb://"
        mongoURL += host + ":" + port + "/" + db
        self.db = MongoClient(mongoURL)[db]

    def checkSudoku(self, sudoku):
        if isinstance(sudoku, dict):
            if "_id" in sudoku:
                del sudoku["_id"]

            if len(sudoku) == 81:
                for section in range(1, 10):
                    sec = "S" + str(section)
                    for position in range(1, 10):
                        pos = sec + "P" + str(position)
                        if type(sudoku[pos]) != int or sudoku[pos] < 0 or sudoku[pos] > 9:
                            raise ValueError("Position " + pos + " is wrong!")
            else:
                raise Exception("Invalid sudoku length")
        else:
            raise Exception("Invalid sudoku format")

    def createSudoku(self):
        sud = Sudoku()
        return sud.getSudoku()

    def insertSudoku(self, board):
        valid = False
        try:
            self.checkSudoku(board)
            if self.db.sudoku.find_one(board) is None:
                result = self.db.sudoku.insert_one(board)
                valid = result.inserted_id
        except Exception as e:
            print(e)
        return valid

    def printCollection(self):
        cursor = self.db.sudoku.find()
        for document in cursor:
            print(document)


def startPoint():
    try:
        db = DataBase("localhost", "27017", "tester", "test", "webui-test")
        keepgoing = True
        while keepgoing:
            sudoku = db.createSudoku()
            keepgoing = db.insertSudoku(sudoku)
        exit(0)
    except KeyboardInterrupt:
        print("Stopped by Keysstroke")
        exit(1)
    except Exception as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    startPoint()
