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

def tags():
    fun = '''
    function(doc) {
      if (doc.tags) {
        var i;
        for (i = 0; i < doc.tags.length; i++)
          emit(doc.tags[i], doc);
      }
    }'''
    return fun

doc = {
  'language' : 'javascript',
  'views' : {
    'inbox'   : { 'map' : _tasks('inbox') },
    'next'    : { 'map' : _tasks('next')  },
    'someday' : { 'map' : _tasks('someday') },
    'trash'   : { 'map' : _tasks('trash') },
    'tags'    : { 'map' : tags() }
  }
}

def load():
    db = Server()['taskbin']
    if db.get('_design/t'):
        _doc = db['_design/t']
        db.delete(_doc)
    db['_design/t'] = doc

def clear():
    """Deletes existing design docs"""
    db = Server()['taskbin']
    _old = db['_design/taskbin']
    db.delete(_old)
    _t = db['_design/t']
    db.delete(_t)

if __name__ == '__main__':
    load()
