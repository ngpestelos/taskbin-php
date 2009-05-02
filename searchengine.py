from couchdb import Server

db = Server()['taskbin']

def get_tasks(word):
    return [r.value for r in db.view('_design/taskbin/_view/words', key=word)]

def find(q):
    words = q.split(' ')
    return get_tasks(words[0])
