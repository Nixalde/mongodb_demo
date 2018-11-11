import pymongo
myclient = pymongo.MongoClient('mongodb://172.22.200.178:27017/')
mydb = myclient["test"]
mycol = mydb["personal"]

for x in mycol.find():
  print(x)
