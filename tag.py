import web
from couchdb import Server
from datetime import datetime
import types

render = web.template.render('static/', base='site')

urls = (
  '/tag', 'Tag'
)

db = Server()['tasks']

def getDocument(name):
    fun = '''
    function(doc) {
      if (doc.type == 'tag' && doc.name == '%s')
        emit(doc._id, doc);
    }''' % (name)
    return [(r.key, r.value) for r in db.query(fun)]

def create(t):
    row = dict(type='tag', name=t, posted=datetime.today().ctime())
    return db.create(row)

def addTask(tagId, taskId):
    tag = db[tagId]
    tag.setdefault('tasks', []).append(taskId)
    db[tagId] = tag

class Tag:
    def POST(self):
        input = web.input()
        doc = getDocument(input.tag)
        id = None
        if doc:
            id = doc[0][0]
        else:
            id = create(input.tag)
        addTask(id, input.task)
        raise web.seeother('/task/%s' % input.task)
