from tornado.ioloop import IOLoop
from tornado.web import Application

from .routes import routes
from .settings import STATIC_PATH, TEMPLATE_PATH

PORT = 8888


def runApp():
    application = Application(routes, debug=True, settings={
        "autoreload": True,
        "template_path": TEMPLATE_PATH,
        "static_path": STATIC_PATH
    })

    application.listen(PORT)
    print(f"\033[92mApp Listening on Port: {PORT}")
    IOLoop.current().start()
