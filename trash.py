import web
from couchdb import Server

urls = (
  '/trash', 'trash.Inbox'
)

render = web.template.render('static/', base='site')

db = Server()['taskbin']

def getItems():
    f = '''
    function(doc) {
      if (doc.type == 'trash')
        emit(Date.parse(doc.posted), doc);
    }'''
    return [(r.id, r.value) for r in db.query(f, descending=True)]

class Inbox:
    def GET(self):
        items = getItems()
        return render.trash(items)
