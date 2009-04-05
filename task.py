from couchdb import Server
from datetime import datetime
import tag

db = Server()['taskbin']

def next():
    fun = "function(doc) { if (doc.type == 'next') emit (doc.posted, doc) }"
    return [r.value for r in db.query(fun)]

def inbox():
    fun = '''function(doc) { if (doc.type == 'in') emit (doc.posted, doc) }'''
    return [r.value for r in db.query(fun)]

def post(task, tags):
    task = {'type' : 'in', 'task' : task, 'posted' : datetime.today().ctime()}
    taskId = db.create(task)
    for t in tags.split(','):
        tag = {'type' : 'tag', 'name' : t.strip(), \
               'posted' : datetime.today().ctime(), 'task' : taskId}
        db.create(tag)

def get(id):
    return db[id]
