#!/usr/bin/env python

import web, web.utils
import task, design, searchengine
from datetime import datetime
import time

urls = (
  '/t/tag/(.*)', 'TaggedTasks',
  '/t/move/(.*)', 'Move',
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

render = web.template.render('static', base='site')

def when_posted(posted):
    parsed = time.strptime(posted, '%a %b %d %H:%M:%S %Y')
    dt = datetime.fromtimestamp(time.mktime(parsed))
    return web.utils.datestr(dt, datetime.today())

class TaggedTasks:
    def GET(self, tagId):
        tag, tasks = task.all_tasks(tagId)
        return render.tagged_tasks(tag, tasks)

class Move:
    def GET(self, id):
        input = web.input()
        if 'trash' in input.t:
            task.move(id, 'trash')
        elif 'someday' in input.t:
            task.move(id, 'someday')
        elif 'next' in input.t:
            task.move(id, 'next')
        raise web.seeother('/t/%s' % input.f)

class Detail:
    def GET(self, taskId):
        t, tags = task.detail(taskId)
        posted = when_posted(t['posted'])
        return render.task_detail(t['task'], t['_id'], t['type'], posted, tags)

class Trash:
    def GET(self):
        return render.trash(task.trash())

class Someday:
    def GET(self):
        return render.someday(task.someday())

class Next:
    def GET(self):
        return render.next(task.next())

class Inbox:
    def GET(self):
        return render.inbox(task.inbox())

class Search:
    def POST(self):
        input = web.input()
        tasks = searchengine.find(input.q)
        return render.search_results(input.q, tasks)

class Tags:
    def GET(self):
        return render.tags(task.all_tags())

class Stuff:
    def POST(self):
        input = web.input()
        task.post(input.task, input.tags)
        raise web.seeother('/t')
    def GET(self):
        return render.stuff()

class Index:
    def GET(self):
        return render.index()

if __name__ == '__main__':
    design.load()
    app.run()
