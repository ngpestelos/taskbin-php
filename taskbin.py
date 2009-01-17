import web
import task, tag
from web.net import websafe

urls = (
  '/someday', 'Someday',
  '/trash', 'Trash',
  '/move/(.*)', 'Move',
  '/tag', 'Tag',
  '/task/(.*)', 'Detail',
  '/inbox', 'Inbox',
  '/post', 'NewStuff',
  '/',  'NewStuff'
)

app = web.application(urls, globals(), autoreload=True)

render = web.template.render('static/', base='site')

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
        raise web.seeother('/')

class Tag:
    def POST(self):
        input = web.input()
        tag.post(input.task, input.tag)
        raise web.seeother('/task/%s' % input.task)

class Detail:
    def GET(self, id):
        return render.task_detail(task.get(id))

class Inbox:
    def GET(self):
        return render.inbox(task.getAll('in'))

class NewStuff:
    def POST(self):
        input = web.input()
        task.post(input.stuff)
        raise web.seeother('/')

    def GET(self):
        tags = tag.getAll()
        return render.new_stuff(tags)

if __name__ == '__main__':
    app.run()
