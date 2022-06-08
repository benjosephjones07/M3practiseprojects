import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://root:Blunderbuss101@cluster0.zj2co.mongodb.net/?retryWrites=true&w=majority")

db = cluster["test"]

collection = db["test"]

post = {"_id": 0, "name": "Ben", "score": 5}

collection.insert_1(post)
