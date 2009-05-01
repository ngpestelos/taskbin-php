from couchdb import Server
import task

db = Server()['taskbin']

def rebuild_tags():
    tasks = [r.value for r in db.view('_design/taskbin/_view/tasks')]
    for t in tasks:
        for tag in t.get('tags', []):
            task.make_tag(tag)       
