import tornado.ioloop
import tornado.web
from handlers import UserHandler, CreateUserHandler, EditUserHandler, DeleteUserHandler

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect('/users')

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/users", UserHandler),  # List users
        (r"/users/create", CreateUserHandler),  # Create a user
        (r"/users/edit/([0-9]+)", EditUserHandler),  # Edit a user
        (r"/users/delete/([0-9]+)", DeleteUserHandler),  # Delete a user
    ], template_path="templates", static_path="static", debug=True, autoreload = True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8881)
    print("Listening on http://localhost:8881")
    tornado.ioloop.IOLoop.current().start()
