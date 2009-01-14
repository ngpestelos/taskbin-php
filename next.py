import web
from couchdb import Server
from utils import getItems

urls = (
  '/next', 'next.Inbox'
)

render = web.template.render('static/', base='site')

db = Server()['taskbin']

class Inbox:
    def GET(self):
        items = getItems('next')
        return render.next(items)
