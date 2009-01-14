import web
from couchdb import Server
from datetime import datetime

urls = (
  '/inbox', 'stuff.Inbox',
  '/post', 'stuff.New'
)

render = web.template.render('static/', base='site')

db = Server()['taskbin']

def getItems():
    f = '''
    function(doc) {
      if (doc.type == 'in')
        emit(Date.parse(doc.posted), doc);
    }'''
    return [(r.id, r.value) for r in db.query(f, descending=True)]

def create(stuff):
    row = dict(type='in', name=stuff, posted=datetime.today().ctime())
    db.create(row)

class Inbox:
    def GET(self):
        items = getItems()
        return render.inbox(items)

class New:
    def POST(self):
        input = web.input()
        create(input.stuff)
        raise web.seeother('/')

    def GET(self):
        return render.new_stuff()
