# based on word_count_views.rb

from couchdb import Server
import simplejson as json

couch = Server()
db = couch['taskbin']

count = {
  'map' : '''
    function(doc) {
      for (var i = 0; i < doc.tags.length; i++)
        emit(doc.tags[i], 1);
    }''',
  'reduce' : '''
    function(key, combine) {
      return sum(combine);
    }'''
}

tasks = {
  'map' : '''
    function(doc) {
      for(var i = 0; i < doc.tags.length; i++)
        emit(doc.tags[i], doc);
    }
  '''
}

try:
  db.delete(db['_design/tags'])
except:
  pass

db['_design/tags'] = {
  'views' : { 'count' : count, 'tasks' : tasks }
}
