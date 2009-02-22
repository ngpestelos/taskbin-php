#!/usr/bin/env python

import web
import task, tag

urls = (
  '/t/(.*)/', 'Redirect',
  '/t/comment', 'Comment',
  '/t/tag/(.*)', 'TagDetail',
  '/t/tag', 'Tag',
  '/t/next', 'Next',
  '/t/someday', 'Someday',
  '/t/trash', 'Trash',
  '/t/move/(.*)', 'Move',
  '/t/task/(.*)', 'Detail',
  '/t/inbox', 'Inbox',
  '/t/post', 'NewStuff',
  '/t', 'NewStuff'
)

app = web.application(urls, globals(), autoreload=True)

render = web.template.render('static/', base='site')

class Comment:
    def POST(self):
        input = web.input()
        task.comment(input.task, input.comment)
        raise web.seeother('/t/task/%s' % input.task)

class TagDetail:
    def GET(self, id):
        (t, tasks) = tag.getTasks(id)
        return render.tag_detail(t, tasks)

class Next:
    def GET(self):
        return render.next(task.getAll('next'))

class Someday:
    def GET(self):
        return render.someday(task.getAll('someday'))

class Trash:
    def GET(self):
        return render.trash(task.getAll('trash'))

class Move:
    def GET(self, id):
        input = web.input()
        if 'trash' in input:
            task.move(id, 'trash')
        elif 'someday' in input:
            task.move(id, 'someday')
        elif 'next' in input:
            task.move(id, 'next')
        raise web.seeother('/t')

class Tag:
    def POST(self):
        input = web.input()
        tag.post(input.task, input.tag)
        raise web.seeother('/t/task/%s' % input.task)

class Detail:
    def GET(self, id):
        return render.task_detail(task.get(id))

class Inbox:
    def GET(self):
        return render.inbox(task.getAll('in'))

class NewStuff:
    def POST(self):
        input = web.input()
        task.post(dict(post=input.stuff, tag=input.tag))
        raise web.seeother('/t')

    def GET(self):
        return render.new_stuff(tag.getAll())

class Redirect:
    def GET(self, path):
        raise web.seeother('/t' + path)

if __name__ == '__main__':
    app.run()
