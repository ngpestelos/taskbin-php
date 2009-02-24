from couchdb import Server

index_db = Server()['taskbin_index']
task_db = Server()['taskbin']

class TooManyTerms(Exception):
    """Exception raised when there are too many search terms"""

def find(words):
    q = words.split(' ')
    if len(q) > 1:
        raise TooManyTerms
    try:
        id = [r.id for r in index_db.view('index/words', key=q[0])][0]
        word = index_db[id]
        for taskId in word['tasks']:
            task = task_db[taskId]
            print (task['name'], task['_id'], task.get('tags', []), task['type'])
    except IndexError:
        print "None found."
