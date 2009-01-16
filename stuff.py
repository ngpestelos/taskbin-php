import web
from couchdb import Server
from datetime import datetime

db = Server()['taskbin']

def post(stuff):
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
        tags = getAllTags()
        return render.new_stuff(tags)
