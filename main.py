__author__ = 'stanley'
import webapp2
import jinja2
import json
import os

INDEX_NAME = 'user_basic'

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render())

class SummernoteHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('summernote.html')
        self.response.write(template.render())

class MapHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('map.html')
        self.response.write(template.render())

class AgendaHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('agenda.html')
        self.response.write(template.render())

class AddDetectiveHandler(webapp2.RequestHandler):
    def post(self):
        print self.request.get('name')
        self.response.headers["Content-Type"] = "application/json"
        res = {
            'code': 200
        }

        print json.dumps(res)
        self.response.write(json.dumps(res))

app = webapp2.WSGIApplication([('/', MainHandler),
                               ('/summernote.html', SummernoteHandler),
                               ('/agenda.html', AgendaHandler),
                               ('/api/addDetective/', AddDetectiveHandler),
                               ('/map.html', MapHandler)], debug=True)