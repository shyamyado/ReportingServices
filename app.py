import tornado.ioloop
import tornado.web
import os


from handlers import ReportHandler as rh

settings = {
		"template_path": os.path.join(os.path.dirname(__file__), "html/templates"),
		"static_path": os.path.join(os.path.dirname(__file__), "html/static"),
		"debug" : True
	}


def make_app():
    return tornado.web.Application([
        (r"/", rh.ReportHandler),
        (r"/index", rh.Index),
    ], **settings )
    # ,

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
