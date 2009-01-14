import web
import stuff, task
import tag, trash
import next, someday

urls = (
  '/',  'stuff.New'
)

urls += stuff.urls
urls += task.urls
urls += tag.urls
urls += trash.urls
urls += next.urls
urls += someday.urls

app = web.application(urls, locals(), autoreload=True)

if __name__ == '__main__':
    app.run()
