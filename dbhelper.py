# coding:utf-8

import pymongo

DATABASE = 'waitercaller'

class DBHelper:
    def __init__(self):
        # create a MongoDB client enable connection
        client = pymongo.MongoClient()
        # specify db name, return the self.db that become a object that enable to run CRUD operation
        self.db = client[DATABASE]

    def get_user(self, email):
        return self.db.users.find_one({'name':email})

    def add_user(self, email, salt, hashed):
