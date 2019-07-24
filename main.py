import webapp2  #connecting to the google app engine yaml file
import jinja2 #connets to the html files
import os #apple operating system
# from google.appengine.api import urlfetch
# import json


#jinja2.Environment is a constructor

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        welcome_page = jinja_env.get_template('index.html')
        self.response.write(welcome_page.render())

class PersonalityTestPage(webapp2.RequestHandler):
    def get(self):
        personality_test_page = jinja_env.get_template('pages/personalitytest.html')
        self.response.write(personality_test_page.render())

class AboutPage(webapp2.RequestHandler):
    def get(self):
        about_page = jinja_env.get_template('pages/about.html')
        self.response.write(about_page.render())

class ConnectionsPage(webapp2.RequestHandler):
    def get(self):
        connections_page = jinja_env.get_template('pages/connections.html')
        self.response.write(connections_page.render())

class ResultsPage(webapp2.RequestHandler):
    def get(self):
        results_page = jinja_env.get_template('pages/results.html')
        self.response.write(results_page.render())

# the app configuration section
app = webapp2.WSGIApplication(
    [('/', WelcomePage), ('/pages/personalitytest', PersonalityTestPage), ('/pages/about', AboutPage), ('/pages/connections', ConnectionsPage), ('/pages/results', ResultsPage)],
    debug = True
)
