import hashlib
from couchdb import Server
import task

db = Server()['taskbin']

def hash(text):
    return hashlib.sha1(text).hexdigest()

def get_tags():
    fun = '''function(doc) {
               if (doc.type == 'tag' && !doc.hash)
                emit(doc._id, doc);
             }'''
    return [r.value for r in db.query(fun)]

def apply_hashes():
    tags = get_tags()
    hashes = [(doc['_id'], hash(doc['name'])) for doc in tags]
    for id, hashed_text in hashes:
        doc = db[id]
        doc['hash'] = hashed_text
        db[id] = doc
