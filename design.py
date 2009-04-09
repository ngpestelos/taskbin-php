from couchdb import Server
import simplejson as json

def _tasks(type):
    fun = '''
    function(doc) {
      if (doc.type == '%s') {
        if (doc.updated)
          emit (Date.parse(doc.updated), doc);
        else
          emit (Date.parse(doc.posted), doc);
      }
    }''' % type
    return fun

doc = {
  'language' : 'javascript',
  'views' : {
    'inbox'   : { 'map' : _tasks('inbox') },
    'next'    : { 'map' : _tasks('next')  },
    'someday' : { 'map' : _tasks('someday') },
    'trash'   : { 'map' : _tasks('trash') },
    'detail'  : {
      'map' : '''function(doc) {
                   if (doc.type != 'tag') {
                      emit([doc._id, 0], doc);
                   }
                   else if (doc.type == 'tag') {
                      emit([doc.task, 1], doc);
                   }
                 }'''
    },
    'tags'    : {
      'map' : '''function(doc) {
                   if (doc.type == 'tag')
                     emit(doc.name, [doc._id, doc]);
                 }'''
    }
  }
}

def load():
    db = Server()['taskbin']
    if db.get('_design/taskbin'):
        _doc = db['_design/taskbin']
        db.delete(_doc)
    db['_design/taskbin'] = doc

if __name__ == '__main__':
    load()
