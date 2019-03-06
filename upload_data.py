from pymongo import MongoClient
import pprint
import json

file = open('data1.json', 'r', encoding="utf8")

data = json.load(file)
client = MongoClient('mongodb://db_usr:juttou100@ds141358.mlab.com:41358/juttou')
db = client['juttou']
collection = db.posts
collection.insert(data)
