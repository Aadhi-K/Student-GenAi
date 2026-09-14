from pymongo import MongoClient


client = MongoClient(
    "mongodb://localhost:27017"
)

db = client["Student_helper"]

mock_test_collection = db["mock_tests"]