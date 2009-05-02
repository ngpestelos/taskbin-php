from couchdb import Server
import re

db = Server()['taskbin']

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
    words = q.split(' ')
    keys = get_keys(words[0])
    out = []
    for k in keys:
        out.extend(get_tasks(k))
    return out
