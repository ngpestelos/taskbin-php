import web
import task
import tag, trash
import next, someday

urls = (
  '/task/(.*)', 'Detail',
  '/inbox', 'Inbox',
  '/post', 'NewStuff',
  '/',  'NewStuff'
)

urls += task.urls
urls += tag.urls
urls += trash.urls
urls += next.urls
urls += someday.urls

app = web.application(urls, globals(), autoreload=True)

render = web.template.render('static/', base='site')

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
        return render.new_stuff(tag.getAll())

if __name__ == '__main__':
    app.run()
