import web
from couchdb import Server
from datetime import datetime
import types

render = web.template.render('static/', base='site')

urls = (
  '/tag/(.*)', 'tag.Detail',
  '/tag', 'tag.Tag'
)

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

def post(id, name):
    task = db[id]
    if 'tags' in task and name in task['tags']:
        return
    task.setdefault('tags', []).append(name)
    db[id] = task 
    makeTag(name)

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
      if (doc.tags) {
        for (var i = 0; i < doc.tags.length; i++) {
          if (doc.tags[i] == '%s')
            emit(doc.posted, doc);
        }
      }
    }''' % tag['name']
    tasks = [r.value for r in db.query(fun, descending=True)]
    return (tag, tasks)
