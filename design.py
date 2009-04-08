from couchdb import Server
import simplejson as json

doc = {
  'language' : 'javascript',
  'views' : {
    'inbox' : {
      'map' : '''function(doc) {
                   if (doc.type == 'inbox') emit(doc.posted, doc);
                 }'''
    },
    'next'  : {
      'map' : '''function(doc) {
                   if (doc.type == 'next') emit(doc.posted, doc);
                 }'''
    },
    'someday' : {
      'map' : '''function(doc) {
                   if (doc.type == 'someday') emit(doc.posted, doc);
                 }'''
    },
    'trash' : {
      'map' : '''function(doc) {
                   if (doc.type == 'trash') emit(doc.posted, doc);
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
