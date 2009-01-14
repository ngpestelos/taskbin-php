import web
from couchdb import Server
from utils import getItems

urls = (
  '/trash', 'trash.Inbox'
)

render = web.template.render('static/', base='site')

db = Server()['taskbin']

class Inbox:
    def GET(self):
        items = getItems('trash')
        return render.trash(items)
