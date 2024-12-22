# utils.py
from pymongo import MongoClient
from django.conf import settings

def get_mongo_client():
    client = MongoClient('mongodb://mongo:27017/')
    return client

def get_mongo_database():
    client = get_mongo_client()
    return client[settings.MONGO_DB['NAME']]
