from couchdb import Server
import task, re

db = Server()['taskbin_index']

stopwords = ['and', 'or', 'the', 'a', 'of', 'to', 'in', 'is', 'it']

def destroy():
    fun = '''
    function(doc) {
      emit(doc._id, doc);
    }'''
    docs = [r.value for r in db.query(fun)]
    for doc in docs:
        db.delete(doc)

def splitwords(text):
    words = [s.lower() for s in re.compile(r'\W+').split(text)]
    return [w for w in words if w not in stopwords]

def getTaskIds():
    fun = '''
    function(doc) {
      if (doc.type == 'task')
        emit(doc._id, doc);
    }'''
    return [r.value['taskid'] for r in db.query(fun)]

def build():
    # add all document IDs
    for type in ['next']:
        [db.create(dict(taskid=t['_id'], type='task')) \
          for t in task.getAll(type)]

    # for each document, split words from names
    for doc in getTaskIds():
        t = task.get(doc)
        print splitwords(t['name'])

if __name__ == '__main__':
    destroy()
    build()
