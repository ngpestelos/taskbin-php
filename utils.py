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

def delete_tags():
    tags = [r.value for r in db.view('_design/taskbin/_view/tags')]
    for doc in tags:
        doc['_deleted'] = True
    db.update(tags) # this will complain about list indices must be integers

def move_tags():
    tags = [r.value for r in db.view('_design/taskbin/_view/tags')]
    for tag in tags:
        t = task.get_task(tag['task'])
        if t:
            t.setdefault('tags', []).append(tag['name'])
            db[tag['task']] = t
