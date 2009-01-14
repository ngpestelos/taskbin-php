import web
from couchdb import Server
from datetime import datetime
from utils import getItems

urls = (
  '/inbox', 'stuff.Inbox',
  '/post', 'stuff.New'
)

render = web.template.render('static/', base='site')

db = Server()['taskbin']

def create(stuff):
    row = dict(type='in', name=stuff, posted=datetime.today().ctime())
    db.create(row)

class Inbox:
    def GET(self):
        items = getItems('in')
        return render.inbox(items)

class New:
    def POST(self):
        input = web.input()
        create(input.stuff)
        raise web.seeother('/')

    def GET(self):
        return render.new_stuff()
