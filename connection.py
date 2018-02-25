#!/usr/bin/env python

from sys import exit
from pymongo import MongoClient
from pymongo import errors


class Connection:
    db = None
    collection = None

    def __init__(self, host, port, db, user, password):
        maxSevSelDelay = 1
        if user and password:
            mongoURL = "mongodb://" + user + ":" + password + "@"
        else:
            mongoURL = "mongodb://"
        mongoURL += host + ":" + port + "/" + db
        try:
            client = MongoClient(
                mongoURL, serverSelectionTimeoutMS=maxSevSelDelay)
            client.server_info()
        except errors.ServerSelectionTimeoutError as err:
            print("Connection to " + host + ":" + port + "/" + db + " failed")
            print(err)
            exit(1)
        else:
            self.db = MongoClient(mongoURL)[db]
            self.collection = self.db.grid

    def insertGrid(self, board):
        valid = False
        try:
            if self.collection.find_one(board) is None:
                result = self.collection.insert_one(board)
                valid = result.inserted_id
        except Exception as e:
            print(e)
            exit(1)
        return valid

    def getGrid(self):
        return self.collection.find_one({}, {'_id': False})
