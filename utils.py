from couchdb import Server

db = Server()['taskbin']

def getItems(type):
    f = '''
    function(doc) {
      if (doc.type && doc.type == '%s')
        emit(Date.parse(doc.posted), doc);
    }''' % (type)
    return [(r.id, r.value) for r in db.query(f, descending=True)]
