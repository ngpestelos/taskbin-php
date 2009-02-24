import stripper
from couchdb import Server

index_db = Server()['taskbin_index']
task_db = Server()['taskbin']

stopwords = ['and', 'or', 'the', 'a', 'of', 'to', 'in', 'is', 'it', 'for', \
  'at', 'on', 'with']

def get_document(word):
    wordindex = [(r.key, r.value) for r in index_db.view('index/words', key=word)]
    if wordindex:
        id = wordindex[0][1]
        return index_db[id]
    else:
        return None

def create_views():
    doc = {
      "language": "javascript",
      "views": {
        "words": {
          "map": """function(doc) {
                      if (doc.word) emit(doc.word, doc._id);
                    }"""
        }
      }
    }
    index_db['_design/index'] = doc

def delete_views():
    del index_db['_design/index']

def create_words():
    tasks = [(r.key, r.value) for r in task_db.view('tasks/names')]
    i = 1
    numtasks = len(tasks)
    for id, name in tasks:
        print "Indexing %d of %d tasks" % (i, numtasks)
        words = stripper.getwords(name)
        indexable = [w for w in words if w not in stopwords]
        for word in indexable:
            doc = get_document(word)
            if doc:
                addtoindex(doc, id)
            else:
                index_db.create({'word': word, 'tasks': [id]})
        i += 1

def delete_words():
    words = [(r.key, r.value) for r in index_db.view('index/words')]
    for word, id in words:
        doc = index_db[id]
        index_db.delete(doc)

def post(taskId, name):
    words = stripper.getwords(name)
    indexable = [w for w in words if w not in stopwords]
    for word in indexable:
        doc = get_document(word)
        if doc:
            addtoindex(doc, taskId)
        else:
            index_db.create({'word': word, 'tasks': [taskId]})

def addtoindex(doc, id):
    doc.setdefault('tasks', [])
    if id not in doc['tasks']:
        doc['tasks'].append(id)
    wordId = doc['_id']
    index_db[wordId] = doc
