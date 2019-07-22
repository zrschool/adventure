import webapp2
import jinja2
import os

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/start.html")
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ("/", MainPage),
])
