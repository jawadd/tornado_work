# importing the main event loop
import tornado.ioloop

# for HTTP requesthandlers ( to map the requests to request handlers)
import tornado.web

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("tornado.html")
        

class PostHandler (tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>This is Post 1 ✍️</h1>")

class HomeHandler (tornado.web.RequestHandler):
    def get(self):
        self.render("home.html")

class WeatherHandler(tornado.web.RequestHandler):
    def get(self):
        # Check if the 'degree' parameter is provided
        degree_param = self.get_argument("degree", None)

        if degree_param is not None:
            try:
                degree = int(degree_param)
                output = "Hot ☀️!" if degree > 20 else "Cold 🌦️"
                drink = "Have some cold water 🍺!" if degree > 20 else "You need a hot beverage ☕"
            except ValueError:
                output = "Invalid degree value. Please enter a valid number."
                drink = ""
        else:
            output = "Please provide a temperature degree. <br> For example, http://127.0.0.1:8888/weather?degree=30"
            drink = ""

        # Passing data to HTML template
        self.render("weather.html", output=output, drink=drink)


def make_app():
    return tornado.web.Application([
        (r"/", HelloHandler),
        (r"/post", PostHandler),
        (r"/home", HomeHandler),
        # expect a url parameter like
        # http://127.0.0.1:8888/weather?degree=30
        (r"/weather", WeatherHandler),
    ], 
    debug = True,
    autoreload = True)



if __name__ == "__main__":
    app = make_app()
    port = 8888
    app.listen(port)
    print(f' Server is listening on localhost on port {8888}')
    # to start ther server on the current thread
    tornado.ioloop.IOLoop.current().start()


