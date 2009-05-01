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
    d = [dict(_id=r.value['_id'], _rev=r.value['_rev'], _deleted=True) for r in db.view('_design/taskbin/_view/tags')]
    to_delete = dict(docs=d)
    import simplejson as json
    import httplib
    headers = {'Content-type' : 'application/json', 'Accept' : 'text/plain'}
    conn = httplib.HTTPConnection('localhost:5984')
    conn.request("POST", "/taskbin/_bulk_docs", json.dumps(d), headers)
    response = conn.getresponse()
    print response.status, response.reason
    conn.close()
