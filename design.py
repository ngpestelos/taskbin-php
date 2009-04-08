from couchdb import Server
import simplejson as json

def load():
    db = Server()['taskbin']
    db['_design/taskbin'] = json.load(file('taskbin.js'))
