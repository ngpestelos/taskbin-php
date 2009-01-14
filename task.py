import web
from couchdb import Server
from tag import getTaskTags

urls = (
  '/task/(.*)', 'task.Detail',
  '/move/(.*)', 'task.Move'
)

db = Server()['taskbin']

render = web.template.render('static/', base='site')

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
