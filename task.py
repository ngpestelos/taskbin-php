from couchdb import Server
from datetime import datetime
import tag

db = Server()['taskbin']

def post(task, tags):
    task = {'type' : 'in', 'task' : task, 'posted' : datetime.today().ctime()}
    taskId = db.create(task)
    for t in tags.split(','):
        tag = {'type' : 'tag', 'name' : t.strip(), \
               'posted' : datetime.today().ctime(), 'task' : taskId}
        db.create(tag)
