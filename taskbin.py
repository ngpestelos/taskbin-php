import web
import task, tag
from web.net import websafe

urls = (
  '/tag', 'Tag',
  '/task/(.*)', 'Detail',
  '/inbox', 'Inbox',
  '/post', 'NewStuff',
  '/',  'NewStuff'
)

app = web.application(urls, globals(), autoreload=True)

render = web.template.render('static/', base='site')

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
