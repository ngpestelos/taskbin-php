from couchdb import Server
import simplejson as json

couch = Server()
db = couch['taskbin']

def by_type(type):
  fun = {
    'map' : '''
      function(doc) {
        if (doc.type == '%s')
          emit(Date.parse(doc.updated), doc);
      }''' % type
  }
  return fun

try:
  db.delete(db['_design/tasks'])
except:
  pass

db['_design/tasks'] = {
  'views' : { 'inbox' : by_type('inbox'), 'someday' : by_type('someday'), 'next' : by_type('next'), 'trash' : by_type('trash') }
}
