import web
import stuff, task
import tag, trash

urls = (
  '/',  'stuff.New'
)

urls += stuff.urls
urls += task.urls
urls += tag.urls
urls += trash.urls

app = web.application(urls, locals(), autoreload=True)

if __name__ == '__main__':
    app.run()
