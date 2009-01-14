from couchdb import Server
# re-mapping

db = Server()['tasks']

def getTasks():
    fun = '''
    function(doc) {
      if (doc.type == 'task')
        emit(doc._id, doc);
    }'''
    return [(r.id, r.value) for r in db.query(fun)]

def getTags():
    fun = '''
    function(doc) {
      if (doc.type == 'task') {
        for (var i = 0; i < doc.tags.length; i++) {
          emit(doc._id, doc.tags[i]);
        }
      }
    }'''
    return [(r.key, r.value) for r in db.query(fun)]

def getTag(tag):
    fun = '''
    function(doc) {
      if (doc.type == 'tag' && doc.name == '%s')
        emit(doc._id, doc);
    }''' % (tag)
    return [r.id for r in db.query(fun)]

def setTags():
    for (taskId, name) in getTags():
        tagId = getTag(name)[0]
        tag = db[tagId]
        tag.setdefault('tasks', []).append(taskId)
        db[tagId] = tag

def removeTagsFromTask():
    for (k, v) in getTasks():
        task = db[k]
        if task.has_key('tags'):
            del task['tags']
            db[k] = task
