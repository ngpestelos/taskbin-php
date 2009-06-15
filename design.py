from couchdb import Server
import simplejson as json

def _tasks(type):
    fun = '''
    function(doc) {
      if (doc.type == '%s') {
        emit (doc._id, doc);
      }
    }''' % type
    return fun

doc = {
  'language' : 'javascript',
  'views' : {
    'inbox'   : { 'map' : _tasks('inbox') },
    'next'    : { 'map' : _tasks('next')  },
    'someday' : { 'map' : _tasks('someday') },
    'trash'   : { 'map' : _tasks('trash') }
  }
}

def load():
    db = Server()['taskbin2']
    if db.get('_design/t'):
        _doc = db['_design/t']
        db.delete(_doc)
    db['_design/t'] = doc

if __name__ == '__main__':
    load()
