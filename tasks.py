import web
from couchdb import Server
from datetime import datetime

render = web.template.render('static/')

urls = (
  '/tag', 'Tag',
  '/task/(.*)', 'Task',
  '/inbox', 'Inbox',
  '/post',  'NewStuff',
  '/',      'Home'
)

app = web.application(urls, locals(), autoreload=True)

db = Server()['tasks']

class Tag:
    def POST(self):
        input = web.input()
        doc = db[input.task]
        if 'tags' in doc:
            tags = doc['tags']
            tags.append(input.tag)
            tags.sort()
            doc['tags'] = tags
        else:
            doc['tags'] = [input.tag]
            print doc['tags']
        db[input.task] = doc 
        raise web.seeother('/task/%s' % input.task)

class Task:
    def GET(self, id):
        doc = db[id]
        return render.site(render.task_detail(doc))

class Inbox:
    def getItems(self):
        f = '''
        function(doc) {
          if (doc.type == 'task')
            emit(doc.posted, doc);
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
