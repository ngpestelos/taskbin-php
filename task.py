from couchdb import Server
from datetime import datetime

db = Server()['taskbin']

def comment(id, comment):
    task = db[id]
    row = {'posted' : datetime.today().ctime(), 'comment' : comment}
    task.setdefault('comments', []).append(row)
    db[id] = task

def post(stuff):
    row = dict(type='in', name=stuff, posted=datetime.today().ctime())
    db.create(row)

def get(id):
    return db[id]

def getAll(type):
    ''' Returns a list of task for a given type.
        Sorts results by latest posting date. '''
    fun = '''
    function(doc) {
      if (doc.type && doc.type == '%s')
        emit(Date.parse(doc.posted), doc);
    }''' % (type)
    return [r.value for r in db.query(fun, descending=True)]

def move(id, newtype):
    task = db[id]
    task['type'] = newtype
    db[id] = task
