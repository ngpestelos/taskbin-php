from couchdb import Server
from datetime import datetime

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

def get(id):
    return db[id]
