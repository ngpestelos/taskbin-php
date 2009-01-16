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

def post(id, name):
    task = db[id]
    if 'tags' in task and name in task['tags']:
        return
    task.setdefault('tags', []).append(name)
    db[id] = task 

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

def getAllTags():
    fun = '''
    function(doc) {
      if (doc.type == 'tag')
        emit(doc.name, doc);
    }'''
    return [(r.id, r.key) for r in db.query(fun)]

def getTaskIds(tagId):
    fun = '''
    function(doc) {
      if (doc.type == 'tasktag' && doc.tag == '%s')
        emit(doc.task, null);
    }''' % (tagId)
    return [r.key for r in db.query(fun)]

def getTasks(id):
    fun = '''
    function(doc) {
      if (doc.type == 'tag' && doc._id == '%s')
        emit([0, doc._id], doc);
      else if (doc.type == 'tasktag' && doc.tag == '%s') {
        if (doc.posted)
          emit([1, doc.posted], doc.task);
        else
          emit([2, doc._id], doc.task);
      }
    }''' % (id, id)
    return [(r.key, r.value) for r in db.query(fun)]

class Detail:
    def GET(self, tagId):
        tasks = getTasks(tagId)
        tag = tasks[0][1]
        tasks = [t[1] for t in tasks[1:]]
        #taskIds = getTaskIds(tagId)
        #tasks = [db[id] for id in taskIds]
        #tasks.sort()
        #return "all tasks for %s" % tagId
        return render.tag_detail(tag, tasks)

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
