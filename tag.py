import web
from couchdb import Server
from datetime import datetime
import types

render = web.template.render('static/', base='site')

urls = (
  '/tag', 'tag.Tag'
)

db = Server()['taskbin']

def getDocument(name):
    fun = '''
    function(doc) {
      if (doc.type == 'tag' && doc.name == '%s')
        emit(doc._id, doc);
    }''' % (name)
    return [(r.key, r.value) for r in db.query(fun)]

def getTaskTags(taskId):
    fun = '''
    function(doc) {
      if (doc.type == 'tasktag' && doc.task == '%s')
        emit(doc.name, doc);
    }''' % (taskId)
    return [(r.value['tag'], r.value['name']) for r in db.query(fun)]

def makeTag(t):
    row = dict(type='tag', name=t, posted=datetime.today().ctime())
    return db.create(row)

def addTask(aTag, taskId):
    row = dict(type='tasktag', tag=aTag['_id'], name=aTag['name'], task=taskId)
    return db.create(row)

class Tag:
    def POST(self):
        input = web.input()
        doc = getDocument(input.tag)
        id = None
        if doc:
            id = doc[0][0]
        else:
            id = makeTag(input.tag)
        addTask(db[id], input.task)
        raise web.seeother('/task/%s' % input.task)
