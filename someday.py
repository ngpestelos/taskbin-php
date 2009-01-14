import web
from couchdb import Server
from utils import getItems

urls = (
  '/someday', 'someday.Inbox'
)

render = web.template.render('static/', base='site')

db = Server()['taskbin']

class Inbox:
    def GET(self):
        items = getItems('someday')
        return render.someday(items)
