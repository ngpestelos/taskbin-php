from couchdb import Server
from datetime import datetime
from sets import Set
import urllib

db = Server()['taskbin']

def move(id, newtype):
    task = db[id]
    task['type'] = newtype
    task['updated'] = datetime.today().ctime()
    db[id] = task

def trash():
    return _view('trash')

def someday():
    return _view('someday')

def next():
    return _view('next')

def inbox():
    return _view('inbox')

def detail(taskId):
    return [r.value for r in db.view('_design/taskbin/_view/detail', \
      startkey=[taskId, 0], endkey=[taskId, 1])]

def _view(type):
    return [r.value for r in db.view('_design/taskbin/_view/%s' % type, \
      descending=True)]

def post(task, tags):
    task = {'type' : 'inbox', 'task' : task, \
      'posted' : datetime.today().ctime()}
    taskId = db.create(task)
    for t in tags.split(','):
        tag = {'type' : 'tag', 'name' : t.strip(), \
               'posted' : datetime.today().ctime(), 'task' : taskId}
        db.create(tag)

def all_tags():
    res = [r.value for r in db.view('_design/taskbin/_view/tags')]
    tags = {}
    for doc in res:
        if 'name' in doc and 'hash' in doc:
            tags[doc['name']] = doc['hash']
    keys = tags.keys()
    keys.sort()
    values = [tags[k] for k in keys]
    return keys, values

def all_tasks(hash):
    q = dict(key=hash)
    ehash = urllib.urlencode(q)
    res = [r for r in db.view('_design/taskbin/_view/by_hash', key=ehash[4:])]

def get(id):
    return db[id]
