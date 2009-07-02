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

def count_map():
    return '''
    function (doc) {
      if (doc.tags) {
        var i;
        for (i = 0; i < doc.tags.length; i++)
          emit(doc.tags[i], 1);
      }        
    }
    '''

def count_reduce():
    return '''
    function(keys, values, rereduce) {
      var tags = {};
      var i;
      for (i = 0; i < keys.length; i++)
        tags[keys[i][0]] = 0;
      var j;
      for (j = 0; j < keys.length; j++) {
        tags[keys[j][0]] += 1;
      }
      return tags;
    }'''


tags_doc = {
  'language' : 'javascript',
  'views' : {
    'count' : { 'map' : count_map(), 'reduce' : count_reduce() }
  }
}


def load_tags():
    """Creates the tags design doc."""
    db = get_db()
    db['_design/tags'] = tags_doc

def clear():
    """Deletes existing design docs"""
    def d(doc):
        db = get_db()
        if db.get(doc):
            db.delete(db[doc])
    d('_design/taskbin')
    d('_design/t')
    d('_design/tags')

def get_db():
    return Server()['taskbin']

if __name__ == '__main__':
    load_tags()
