import os
import json
import webapp2
import jinja2
from urllib import urlencode
from google.appengine.api import urlfetch

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/main.html')
        self.response.write(template.render())


class SearchHandler(webapp2.RequestHandler):
    def post(self):
        filter = self.request.get('filter')
        base_url = 'https://ghibliapi.herokuapp.com/{}'.format(filter)
        response = json.loads(urlfetch.fetch(base_url).content)
        template = jinja_env.get_template('templates/result.html')
        self.response.write(template.render({ 'response': response }))

app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/search', SearchHandler),
], debug=True)
