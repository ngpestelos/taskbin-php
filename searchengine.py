from couchdb import Server

db = Server()['taskbin_index']

def findDocIds(term):
    fun = '''
    function(doc) {
      if (doc.word && doc.word == '%s')
        emit(doc.docId, null);
    }''' % term
    return [r.key for r in db.query(fun)]

if __name__ == '__main__':
    print findDocIds('program')
