from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27017"
client = MongoClient(MONGO_URL)
db = client["TheWeeklySerb"]

categories_collection = db["categories"]
