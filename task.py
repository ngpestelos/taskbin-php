import web
from couchdb import Server

urls = (
  '/task/(.*)', 'task.Detail',
  '/move/(.*)', 'task.Move'
)

db = Server()['taskbin']

render = web.template.render('static/', base='site')

def post(stuff):
    row = dict(type='in', name=stuff, posted=datetime.today().ctime())
    db.create(row)

def getAll(type):
    fun = '''
    function(doc) {
      if (doc.type && doc.type == '%s')
        emit(Date.parse(doc.posted), doc);
    }''' % (type)
    return [r.value for r in db.query(fun)]

def move(id, newtype):
    task = db[id]
    task['type'] = newtype
    db[id] = task

class Move:
    def GET(self, id):
        #return "moving %s to %s" % (id, web.input().b) 
        input = web.input()
        if 'trash' in input:
            move(id, 'trash')
        elif 'someday' in input:
            move(id, 'someday')
        elif 'next' in input:
            move(id, 'next')
        raise web.seeother('/') 

class Detail:
    def GET(self, id):
        tags = getTaskTags(id)
        return render.task_detail(db[id], tags)
