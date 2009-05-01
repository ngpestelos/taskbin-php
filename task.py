from couchdb import Server
from datetime import datetime
from sets import Set
import utils
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

def make_tag(tag):
    if [r for r in db.view('_design/taskbin/_view/tags', key=tag)]:
        pass
    else:
        db.create({'type' : 'tag', 'name' : tag, 'posted': datetime.today().ctime()})

def post(task, tags):
    stripped_tags = [t.strip() for t in tags.split(',')]
    task = {'type' : 'inbox', 'task' : task, \
      'posted' : datetime.today().ctime(), 'tags' : stripped_tags}
    db.create(task)
    for tag in stripped_tags:
        make_tag(tag)

def all_tags():
    return [r.value for r in db.view('_design/taskbin/_view/tags')]
    
def all_tasks(hash):
    q = dict(key=hash)
    ehash = urllib.urlencode(q)
    res = [r.value['task'] for r in db.view('_design/taskbin/_view/by_hash', key=ehash[4:])]
    return [db[id] for id in res]

def get_tag(hash):
    q = dict(key=hash)
    ehash = urllib.urlencode(q)
    tags = [r.value for r in db.view('_design/taskbin/_view/by_hash', key=ehash[4:])]
    return tags[0]

def get(id):
    return db[id]
