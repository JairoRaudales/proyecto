import pymongo
import os

from webapi.dbclasses.dbmongo import DbMongo

class ClienteCollection:

    def __init__(self):
        self.client, self.db = DbMongo.getDB()
        self.collection = "webapi_cliente"

    def getOne(self, id):
        collection = self.db[self.collection]
        return collection.find_one({"id_nacional": id})