from couchdb import Server
from datetime import datetime
import tag, indexer

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
    indexer.post(id, stuff['post'])

def get(id):
    return db[id]

def getAll(type):
    ''' Returns a list of tasks for a given type.

        Sorts results by latest posting date. '''
    def _tasks(type):
        return [r.value for r in db.view('tasks/%s' % type, descending=True)]

    if type == 'in':
        return _tasks('in')
    elif type == 'someday':
        return _tasks('someday')
    elif type == 'next':
        return _tasks('next')
    elif type == 'trash':
        return _tasks('trash')
    else:
        return []

def move(id, newtype):
    task = db[id]
    task['type'] = newtype
    task['updated'] = datetime.today().ctime()
    db[id] = task

def create_views():
    doc = {
      "language": "javascript",
      "views": {
        "in": {
          "map": """function(doc) {
                      if (doc.type == 'in') emit(Date.parse(doc.posted), doc);
                    }"""
        },
        "someday": {
          "map": """function(doc) {
                      if (doc.type == 'someday')
                        emit(Date.parse(doc.posted), doc);
                    }"""
        },
        "next": {
          "map": """function(doc) {
                      if (doc.type == 'next')
                        emit(Date.parse(doc.posted), doc);
                    }"""
        },
        "trash": {
          "map": """function(doc) {
                      if (doc.type == 'trash')
                        emit(Date.parse(doc.posted), doc);
                    }"""
        },
        "names": {
          "map": """function(doc) {
                      if (doc.name)
                        emit(doc._id, doc.name);
                    }"""
        }
      }
    }
    db['_design/tasks'] = doc

def delete_views():
    del db['_design/tasks']
