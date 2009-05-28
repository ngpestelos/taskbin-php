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
    'tags'    : {
      'map' : '''function(doc) {
                   if (doc.type == 'tag')
                     emit(doc.name, doc);
                 }'''
    },
    'by_tag'  : {
      'map' : '''function(doc) {
                   var type = /someday|inbox|next|trash/.test(doc.type);
                   if (type && doc.tags) {
                     var i;
                     for (i = 0; i < doc.tags.length; i += 1)
                       emit(doc.tags[i], doc);
                   }
                 }''' 
    },
    'tasks'   : {
      'map' : '''function(doc) {
                   var type = /someday|inbox|next|trash/.test(doc.type);
                   if (type) {
                     emit(doc._id, doc);
                   }
                 }'''
    },
    'words'   : {
      'map' : '''function(doc) {
                   if (doc.task) {
                     var w = doc.task.split(/\W+/);
                     for (var i = 0; i < w.length; i++)
                       emit(w[i].toLowerCase(), doc);
                   }
                 }'''
    },
    'words_only' : {
      'map' : '''function(doc) {
                   if (doc.task) {
                     var w = doc.task.split(/\W+/);
                     for (var i = 0; i < w.length; i++)
                       emit(w[i].toLowerCase(), null);
                   }
                 }'''
    },
    'search' : {
      'map' : '''function(doc) {
                   if (doc.type == 'search')
                     emit(doc._id, doc);
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
