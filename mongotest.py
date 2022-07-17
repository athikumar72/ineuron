import pymongo



client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.m5qyjjj.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)


d =  {
     "name" : "sudhanshu",
     "email" : "sudhanshu@ineuroan.ai",
     "surname" : "kumar"
}


db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)



