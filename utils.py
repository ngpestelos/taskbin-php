import hashlib

from couchdb import Server

db = Server()['taskbin']

def apply_hashes(tags):
    for t in tags:
        id = t[0]
        doc = t[1]
        hash = hashlib.sha1(doc['name']).hexdigest()
        doc['hash'] = hashlib.sha1(doc['name']).hexdigest()
        db[id] = doc
