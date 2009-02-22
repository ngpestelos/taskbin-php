from couchdb import Server
from datetime import datetime
import types

db = Server()['taskbin']

def get(name):
    fun = '''
    function(doc) {
      if (doc.type == 'tag' && doc.name == '%s')
        emit(doc._id, doc);
    }''' % name
    return [(r.key, r.value['name']) for r in db.query(fun)]

def makeTag(name):
    if get(name):
        return
    else:
        db.create({'type': 'tag', 'name' : name, 'posted' : \
          datetime.today().ctime()})

def post(id, tagname):
    if tagname:
        task = db[id] 
        if 'tags' in task and tagname in task['tags']:
            return
        task.setdefault('tags', []).append(tagname)
        task['updated'] = datetime.today().ctime()
        db[id] = task 
        makeTag(tagname)

def getAll():
    fun = '''
    function(doc) {
      if (doc.type == 'tag')
        emit(doc.name, doc);
    }'''
    return [(r.id, r.key) for r in db.query(fun)]

def getTasks(id):
    tag = db[id]
    fun = '''
    function(doc) {
      if (doc.tags && doc.type != 'trash') {
        for (var i = 0; i < doc.tags.length; i++) {
          if (doc.tags[i] == '%s' && doc.updated)
            emit(Date.parse(doc.updated), doc);
          else if (doc.tags[i] == '%s')
            emit(Date.parse(doc.posted), doc);
        }
      }
    }''' % (tag['name'], tag['name'])
    tasks = [r.value for r in db.query(fun, descending=True)]
    return (tag, tasks)

def create_views():
    pass

def delete_views():
    pass
