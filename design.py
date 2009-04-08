from couchdb import Server
import simplejson as json

def load():
    db = Server()['taskbin']
    if not db.get('_design/taskbin'):
        db['_design/taskbin'] = json.load('taskbin.js')
