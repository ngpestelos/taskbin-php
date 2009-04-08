from couchdb import Server
from datetime import datetime

db = Server()['taskbin']

def move(id, newtype):
    task = db[id]
    task['type'] = newtype
    task['updated'] = datetime.today().ctime()
    db[id] = task

def trash():
    fun = "function(doc) { if (doc.type == 'trash') emit (doc.posted, doc) }"
    return [r.value for r in db.query(fun)]

def someday():
    fun = "function(doc) { if (doc.type == 'someday') emit (doc.posted, doc) }"
    return [r.value for r in db.query(fun)]

def next():
    fun = "function(doc) { if (doc.type == 'next') emit (doc.posted, doc) }"
    return [r.value for r in db.query(fun)]

def inbox():
    fun = '''function(doc) { if (doc.type == 'inbox') emit (doc.posted, doc) }'''
    return [r.value for r in db.query(fun)]

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
