import web
import stuff, task
import tag, trash
import next, someday

urls = (
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

class Inbox:
    def GET(self):
        return render.inbox(task.getAll('in'))

class NewStuff:
    def POST(self):
        input = web.input()
        stuff.post(input.stuff)
        raise web.seeother('/')

    def GET(self):
        return render.new_stuff(tag.getAll())

if __name__ == '__main__':
    app.run()
