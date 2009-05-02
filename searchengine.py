from couchdb import Server
import re
from datetime import datetime

db = Server()['taskbin']

def save_query(q):
    db.create({'type' : 'search', 'q' : q, 'posted' : datetime.today().ctime()})

def filter_keys(keys):
    matches = {}
    for k in keys:
        matches[k] = 0
    keys2 = matches.keys()
    keys2.sort()
    return keys2

def get_keys(word):
    keys = [r.key for r in db.view('_design/taskbin/_view/words_only')]
    if len(word) == 1:
        return filter_keys([k for k in keys if re.search("^" + word, k)])
    else:
        return filter_keys([k for k in keys if re.search(word, k)])

def get_tasks(word):
    return [r.value for r in db.view('_design/taskbin/_view/words', key=word)]

def find(q):
    save_query(q)
    words = q.split(' ')
    keys = get_keys(words[0]) # TODO multi-word search
    out = []
    for k in keys:
        out.extend(get_tasks(k))
    return out
