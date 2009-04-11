import hashlib
from couchdb import Server
import task

db = Server()['taskbin']

def get_tags():
    fun = '''function(doc) {
               if (doc.type == 'tag' && !doc.hash)
                emit(doc._id, doc);
             }'''
    return [r.value for r in db.query(fun)]

def apply_hashes():
    tags = get_tags()
    hashes = [(doc['_id'], hashlib.sha1(doc['name']).hexdigest()) \
        for doc in tags]
    for id, hash in hashes:
        doc = db[id]
        doc['hash'] = hash
        db[id] = doc
