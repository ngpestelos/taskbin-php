import stripper
from couchdb import Server

index_db = Server()['taskbin_index']
task_db = Server()['taskbin']

stopwords = ['and', 'or', 'the', 'a', 'of', 'to', 'in', 'is', 'it', 'for', \
  'at', 'on', 'with']

def get_document(word):
    wordindex = [(r.key, r.value) for r in \
      index_db.view('index/words', key=word)]
    if wordindex:
        id = wordindex[0][1]
        return index_db[id]
    else:
        id = index_db.create({'word': word})
        return index_db[id]

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

def addtoindex(words, taskId):
    for word in words:
        doc = get_document(word)
        doc.setdefault('tasks', [])
        if taskId not in doc['tasks']:
            doc['tasks'].append(taskId)
            id = doc['_id']
            index_db[id] = doc

def create_words():
    tasks = [(r.key, r.value) for r in task_db.view('tasks/names')]
    i = 1
    numtasks = len(tasks)
    for id, name in tasks:
        print "Indexing %d of %d tasks" % (i, numtasks)
        words = stripper.getwords(name)
        addtoindex(words, id)
        i += 1

def delete_words():
    words = [(r.key, r.value) for r in index_db.view('index/words')]
    for word, id in words:
        doc = index_db[id]
        index_db.delete(doc)
