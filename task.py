from couchdb import Server
from datetime import datetime
from sets import Set

db = Server()['taskbin']

def move(id, newtype):
    task = db[id]
    task['type'] = newtype
    task['updated'] = datetime.today().ctime()
    db[id] = task

def trash():
    return _view('trash')

def someday():
    return _view('someday')

def next():
    return _view('next')

def inbox():
    return _view('inbox')

def detail(taskId):
    task = db[taskId]
    tags = [get_tag(t) for t in task.get('tags', [])]
    return task, tags

def _view(type):
    return [r.value for r in db.view('_design/taskbin/_view/%s' % type, \
      descending=True)]

def make_tag(tag):
    if [r for r in db.view('_design/taskbin/_view/tags', key=tag)]:
        pass
    else:
        db.create({'type' : 'tag', 'name' : tag, 'posted': datetime.today().ctime()})

def get_tag(name):
    res = [r.value for r in db.view('_design/taskbin/_view/tags', key=name)]
    if res:
        return res[0]
    else:
        return None

def post(task, tags):
    stripped_tags = [t.strip() for t in tags.split(',')]
    task = {'type' : 'inbox', 'task' : task, \
      'posted' : datetime.today().ctime(), 'tags' : stripped_tags}
    db.create(task)
    for tag in stripped_tags:
        make_tag(tag)

def all_tags():
    return [r.value for r in db.view('_design/taskbin/_view/tags')]
    
def all_tasks(tagId):
    tag = db[tagId]
    tasks = [db[r.value] for r in db.view('_design/taskbin/_view/by_tag',key=tag['name'])]
    return tag, tasks

def get_task(taskId):
    res = [r.value for r in db.view('_design/taskbin/_view/tasks', key=taskId)]
    if res:
        return res[0]
    else:
        return None
