from couchdb import Server

index_db = Server()['taskbin_index']
task_db = Server()['taskbin']

def get_document(taskId):
    return task_db[taskId]

def find(words):
    q = words.split(' ')
    firstrow = [r.id for r in index_db.view('index/words', key=q[0])]
    if not firstrow:
        return []

    doc = index_db[firstrow[0]]
    tasks = doc.get('tasks', '')
    for n in q[1:]:
        nextrow = [r.id for r in index_db.view('index/words', key=n)]
        if not nextrow:
            return []

        nextdoc = index_db[nextrow[0]]
        nexttasks = []
        for task in tasks:
            if task in nextdoc.get('tasks', []):
                nexttasks.append(task)
        tasks = nexttasks
        if not tasks:
            return []

    return [get_document(id) for id in tasks]
