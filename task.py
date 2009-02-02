from couchdb import Server
from datetime import datetime
import tag

db = Server()['taskbin']

def comment(id, comment):
    task = db[id]
    comment = {'posted' : datetime.today().ctime(), 'comment' : comment}
    task.setdefault('comments', []).append(comment)
    task['updated'] = datetime.today().ctime()
    db[id] = task

def post(stuff):
    task = dict(type='in', name=stuff['post'], posted=datetime.today().ctime())
    id = db.create(task)
    tag.post(id, stuff['tag'])

def get(id):
    return db[id]

def getAll(type):
    ''' Returns a list of task for a given type.
        Sorts results by latest posting date. '''
    fun = '''
    function(doc) {
      if (doc.type == '%s' && doc.updated)
        emit(Date.parse(doc.updated), doc);
      else
        emit(Date.parse(doc.posted), doc);
    }''' % (type)
    return [r.value for r in db.query(fun, descending=True)]

def move(id, newtype):
    task = db[id]
    task['type'] = newtype
    task['updated'] = datetime.today().ctime()
    db[id] = task
