import pymongo


_db = pymongo.MongoClient()['rafter']


def get_db():
    return _db
