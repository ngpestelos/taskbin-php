import web
from couchdb import Server
from datetime import datetime
import types

render = web.template.render('static/', base='site')

urls = (
  '/tag', 'Tag'
)

db = Server()['tasks']

def _getTags(taskId):
    fun = '''
    function(doc) {
      if (doc.tags && doc._id == '%s')
        emit(doc._id, doc.tags);
    }''' % (taskId)
    return [r.value for r in db.query(fun)]

def _getTasks():
    fun = '''
    function(doc) {
      if (doc.type == 'task')
        emit(doc._id, null);
    }
    '''
    return [r.key for r in db.query(fun)]

def _exists(tag):
    fun = '''
    function(doc) {
      if (doc.type == 'tag' && doc.name == '%s')
        emit(doc._id, null);
    }''' % (tag)
    tag = [r.key for r in db.query(fun)]
    if tag:
        return True
    else:
        return False

def _create(tag):
    row = dict(type = 'tag', name = tag, posted = datetime.today().ctime())
    db.create(row)

# python cookbook
def _flatten(sequence, scalarp, result = None):
    if result is None: return []
    for item in sequence:
        if scalarp(item): result.append(item)
        else: _flatten(item, scalarp, result)

def getAllTags():
    alltags = []
    def is_tag(x):
        return type(x) == types.StringType
    for taskId in _getTasks():
        tags = _getTags(taskId)
        _flatten(tags, is_tag, alltags)
    return list(set(alltags))

def makeTags():
    tags = getAllTags()
    for t in tags:
        _create(t)

def flushTags():
    for id in db:
        doc = db[id]
        if doc['type'] == 'tag':
            db.delete(doc)

class Tag:
    def append(self, tags, tag):
        if tag in tags:
            return tags
        else:
            tags.append(tag)
            tags.sort()
            return tags

    def POST(self):
        input = web.input()
        doc = db[input.task]
        if 'tags' in doc:
            tags = self.append(doc['tags'], input.tag)
            doc['tags'] = tags
        else:
            doc['tags'] = [input.tag]
        db[input.task] = doc
        raise web.seeother('/task/%s' % input.task)
