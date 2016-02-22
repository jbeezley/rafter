import pymongo

from .config import mongo_config

_client = None
_db = None


def get_connection():
    global _client
    if _client is None:
        _client = pymongo.MongoClient(
            mongo_config['MONGO_HOST'], mongo_config['MONGO_PORT']
        )
    return _client


def get_db():
    global _db
    if _db is None:
        _db = get_connection()[mongo_config['MONGO_DBNAME']]
    return _db
