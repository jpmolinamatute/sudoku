#!/usr/bin/env python

import sys
import itertools
from bson.objectid import ObjectId
from pymongo import MongoClient
from PyQt5.QtWidgets import (QWidget, QPushButton, QToolTip, QDesktopWidget, QApplication, QGridLayout)
from PyQt5.QtGui import (QFont, QIcon)


class Example(QWidget):
    gridMap = {
        "S1P1": {
            "xAxis": 0,
            "yAxis": 0
        },
        "S1P2": {
            "xAxis": 1,
            "yAxis": 0
        },
        "S1P3": {
            "xAxis": 2,
            "yAxis": 0
        },
        "S1P4": {
            "xAxis": 0,
            "yAxis": 1
        },
        "S1P5": {
            "xAxis": 1,
            "yAxis": 1
        },
        "S1P6": {
            "xAxis": 2,
            "yAxis": 1
        },
        "S1P7": {
            "xAxis": 0,
            "yAxis": 2
        },
        "S1P8": {
            "xAxis": 1,
            "yAxis": 2
        },
        "S1P9": {
            "xAxis": 2,
            "yAxis": 2
        },
        "S2P1": {
            "xAxis": 3,
            "yAxis": 0
        },
        "S2P2": {
            "xAxis": 4,
            "yAxis": 0
        },
        "S2P3": {
            "xAxis": 5,
            "yAxis": 0
        },
        "S2P4": {
            "xAxis": 3,
            "yAxis": 1
        },
        "S2P5": {
            "xAxis": 4,
            "yAxis": 1
        },
        "S2P6": {
            "xAxis": 5,
            "yAxis": 1
        },
        "S2P7": {
            "xAxis": 3,
            "yAxis": 2
        },
        "S2P8": {
            "xAxis": 4,
            "yAxis": 2
        },
        "S2P9": {
            "xAxis": 5,
            "yAxis": 2
        },
        "S3P1": {
            "xAxis": 6,
            "yAxis": 0
        },
        "S3P2": {
            "xAxis": 7,
            "yAxis": 0
        },
        "S3P3": {
            "xAxis": 8,
            "yAxis": 0
        },
        "S3P4": {
            "xAxis": 6,
            "yAxis": 1
        },
        "S3P5": {
            "xAxis": 7,
            "yAxis": 1
        },
        "S3P6": {
            "xAxis": 8,
            "yAxis": 1
        },
        "S3P7": {
            "xAxis": 6,
            "yAxis": 2
        },
        "S3P8": {
            "xAxis": 7,
            "yAxis": 2
        },
        "S3P9": {
            "xAxis": 8,
            "yAxis": 2
        },
        "S4P1": {
            "xAxis": 0,
            "yAxis": 3
        },
        "S4P2": {
            "xAxis": 1,
            "yAxis": 3
        },
        "S4P3": {
            "xAxis": 2,
            "yAxis": 3
        },
        "S4P4": {
            "xAxis": 0,
            "yAxis": 4
        },
        "S4P5": {
            "xAxis": 1,
            "yAxis": 4
        },
        "S4P6": {
            "xAxis": 2,
            "yAxis": 4
        },
        "S4P7": {
            "xAxis": 0,
            "yAxis": 5
        },
        "S4P8": {
            "xAxis": 1,
            "yAxis": 5
        },
        "S4P9": {
            "xAxis": 2,
            "yAxis": 5
        },
        "S5P1": {
            "xAxis": 3,
            "yAxis": 3
        },
        "S5P2": {
            "xAxis": 4,
            "yAxis": 3
        },
        "S5P3": {
            "xAxis": 5,
            "yAxis": 3
        },
        "S5P4": {
            "xAxis": 3,
            "yAxis": 4
        },
        "S5P5": {
            "xAxis": 4,
            "yAxis": 4
        },
        "S5P6": {
            "xAxis": 5,
            "yAxis": 4
        },
        "S5P7": {
            "xAxis": 3,
            "yAxis": 5
        },
        "S5P8": {
            "xAxis": 4,
            "yAxis": 5
        },
        "S5P9": {
            "xAxis": 5,
            "yAxis": 5
        },
        "S6P1": {
            "xAxis": 6,
            "yAxis": 3
        },
        "S6P2": {
            "xAxis": 7,
            "yAxis": 3
        },
        "S6P3": {
            "xAxis": 8,
            "yAxis": 3
        },
        "S6P4": {
            "xAxis": 6,
            "yAxis": 4
        },
        "S6P5": {
            "xAxis": 7,
            "yAxis": 4
        },
        "S6P6": {
            "xAxis": 8,
            "yAxis": 4
        },
        "S6P7": {
            "xAxis": 6,
            "yAxis": 5
        },
        "S6P8": {
            "xAxis": 7,
            "yAxis": 5
        },
        "S6P9": {
            "xAxis": 8,
            "yAxis": 5
        },
        "S7P1": {
            "xAxis": 0,
            "yAxis": 6
        },
        "S7P2": {
            "xAxis": 1,
            "yAxis": 6
        },
        "S7P3": {
            "xAxis": 2,
            "yAxis": 6
        },
        "S7P4": {
            "xAxis": 0,
            "yAxis": 7
        },
        "S7P5": {
            "xAxis": 1,
            "yAxis": 7
        },
        "S7P6": {
            "xAxis": 2,
            "yAxis": 7
        },
        "S7P7": {
            "xAxis": 0,
            "yAxis": 8
        },
        "S7P8": {
            "xAxis": 1,
            "yAxis": 8
        },
        "S7P9": {
            "xAxis": 2,
            "yAxis": 8
        },
        "S8P1": {
            "xAxis": 3,
            "yAxis": 6
        },
        "S8P2": {
            "xAxis": 4,
            "yAxis": 6
        },
        "S8P3": {
            "xAxis": 5,
            "yAxis": 6
        },
        "S8P4": {
            "xAxis": 3,
            "yAxis": 7
        },
        "S8P5": {
            "xAxis": 4,
            "yAxis": 7
        },
        "S8P6": {
            "xAxis": 5,
            "yAxis": 7
        },
        "S8P7": {
            "xAxis": 3,
            "yAxis": 8
        },
        "S8P8": {
            "xAxis": 4,
            "yAxis": 8
        },
        "S8P9": {
            "xAxis": 5,
            "yAxis": 8
        },
        "S9P1": {
            "xAxis": 6,
            "yAxis": 6
        },
        "S9P2": {
            "xAxis": 7,
            "yAxis": 6
        },
        "S9P3": {
            "xAxis": 8,
            "yAxis": 6
        },
        "S9P4": {
            "xAxis": 6,
            "yAxis": 7
        },
        "S9P5": {
            "xAxis": 7,
            "yAxis": 7
        },
        "S9P6": {
            "xAxis": 8,
            "yAxis": 7
        },
        "S9P7": {
            "xAxis": 6,
            "yAxis": 8
        },
        "S9P8": {
            "xAxis": 7,
            "yAxis": 8
        },
        "S9P9": {
            "xAxis": 8,
            "yAxis": 8
        }
    }
    db = MongoClient("mongodb://tester:test@localhost:27017/webui-test")["webui-test"]

    def __init__(self):
        super().__init__()
        self.initUI()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def getBoard(self):
        return self.db.sudoku.find_one({"_id": ObjectId("59a840360df34b2c57398e98")})

    def createGrid(self):
        grid = QGridLayout()
        self.setLayout(grid)
        board = self.getBoard()
        for i, j in itertools.product(range(9), repeat=2):
            index = "S" + str(i + 1) + "P" + str(j + 1)
            label = board[index]
            position = self.gridMap[index]
            button = QPushButton(str(label))
            button.setFixedWidth(30)
            grid.addWidget(button, position["yAxis"], position["xAxis"])

    def initUI(self):
        self.setWindowTitle('Sudoku')
        self.resize(300, 300)
        self.setWindowIcon(QIcon('web.png'))
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('<b>Sudoku</b> Game')
        self.createGrid()
        # btn = QPushButton('1', self)
        # btn.setToolTip('S1P1')
        # btn.resize(30, 30)
        # btn.move(0, 0)
        self.center()
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
