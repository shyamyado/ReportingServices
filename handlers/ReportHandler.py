import tornado.web
# STATIC_PATH = os.path.join(dirname, 'static')
# TEMPLATE_PATH = os.path.join(dirname, 'templates')


class ReportHandler(tornado.web.RequestHandler):
    # SUPPORTED_METHODS = ("GET", "POST")
    def get(self):
        self.write("Hello, world!")

class Index(tornado.web.RequestHandler):
    def get(self):
        # self.write("Hello, Index page!")
        self.render("index.html")
        # self.redirect("index.html")
