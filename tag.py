import web
from couchdb import Server

render = web.template.render('static/', base='site')

urls = (
  '/tag', 'Tag'
)

db = Server()['tasks']

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
