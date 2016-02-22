import cherrypy
from bson import ObjectId

from ..db import get_db


class Base(object):

    """A simple CRUD implementation on top of mongo."""

    collection = None

    def to_json(self, doc):
        if doc is None:
            return None
        elif doc.get('_id'):
            doc['_id'] = str(doc['_id'])
        return doc

    def from_json(self, doc):
        if doc is None:
            return None
        elif doc.get('_id'):
            doc['_id'] = ObjectId(doc['_id'])
        return doc

    def objectid(self, id):
        try:
            id = ObjectId(id)
        except Exception:
            id = None
        return id

    def get_db(self):
        return get_db()

    def get_collection(self):
        assert self.collection is not None
        return self.get_db()[self.collection]

    def create(self, doc):
        col = self.get_collection()
        doc = self.from_json(doc)
        doc['_id'] = col.insert_one(doc).inserted_id
        return self.to_json(doc)

    def read(self, id=None, **kw):
        col = self.get_collection()
        if id is None:
            return [self.to_json(doc) for doc in col.find(kw)]
        else:
            doc = self.to_json(col.find_one({'_id': self.objectid(id)}))
            if doc is None:
                cherrypy.response.status = 404
            return doc

    def update(self, id, doc):
        col = self.get_collection()
        doc = self.from_json(doc)
        if col.replace_one({'_id': self.objectid(id)}, doc).matched_count == 0:
            doc = None
        return self.to_json(doc)

    def delete(self, id):
        col = self.get_collection()
        return col.delete_one({'_id': self.objectid(id)}).deleted_count > 0
