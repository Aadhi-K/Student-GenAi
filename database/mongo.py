from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db=client["Student_helper"]
users_collection =db["users"] 
student_collection=db["Student"]