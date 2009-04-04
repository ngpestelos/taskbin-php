#!/usr/bin/env python

import web
import task, tag
#import searchengine

urls = (
  '/t/task/(.*)', 'Detail',
  '/t/trash', 'Trash',
  '/t/someday', 'Someday',
  '/t/next', 'Next',
  '/t/inbox', 'Inbox',
  '/t/search', 'Search',
  '/t/tags', 'Tags',
  '/t/new', 'Stuff',
  '/t/?',   'Index'
)

app = web.application(urls, globals(), autoreload=True)

render = web.template.render('html', base='site')
render_bare = web.template.render('html')

class Detail:
    def GET(self, taskId):
        doc = task.get(taskId)
        name = doc['task']
        id = doc['_id']
        type = doc['type']
        posted = doc['posted']
        tags = []
        return render.task_detail(name, id, type, posted, tags)

class Trash:
    def GET(self):
        return "trash"

class Someday:
    def GET(self):
        return "someday"

class Next:
    def GET(self):
        return "next"

class Inbox:
    def GET(self):
        return render.inbox(task.inbox())

class Search:
    def POST(self):
        input = web.input()
        return "search is disabled"

class Tags:
    def GET(self):
        return "tags"

class Stuff:
    def POST(self):
        input = web.input()
        task.post(input.task, input.tags)
        raise web.seeother('/t')
    def GET(self):
        return render.stuff()

class Index:
    def GET(self):
        return render_bare.index()

if __name__ == '__main__':
    app.run()
