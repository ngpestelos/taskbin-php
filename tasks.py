import web
from couchdb import Server
from datetime import datetime
import tag

render = web.template.render('static/')

urls = (
  '/tag', 'tag.Tag',
  '/task/(.*)', 'Task',
  '/inbox', 'Inbox',
  '/post',  'NewStuff',
  '/',      'Home'
)

app = web.application(urls, locals(), autoreload=True)

db = Server()['tasks']

urls += tag.urls

class Task:
    def GET(self, id):
        doc = db[id]
        return render.site(render.task_detail(doc))

class Inbox:
    def getItems(self):
        f = '''
        function(doc) {
          if (doc.type == 'task')
            emit(Date.parse(doc.posted), doc);
        }'''
        return [(r.id, r.value['name']) for r in db.query(f, descending=True)]

    def GET(self):
        items = self.getItems()
        return render.site(render.inbox(items))

class NewStuff:
    def POST(self):
        input = web.input()
        db.create({'type' : 'task', 'name' : input.entry, \
          'posted' : datetime.today().ctime()})
        raise web.seeother('/')

class Home:
    def GET(self):
        return render.site(render.home()) 

if __name__ == '__main__':
    app.run()
