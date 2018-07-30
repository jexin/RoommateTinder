import webapp2
import jinja2
import os
import logging
import time

from google.appengine.ext import ndb
from google.appengine.api import users

class Person(ndb.Model):
    name = ndb.StringProperty()
    biography = ndb.StringProperty()
    birthday = ndb.DateProperty()
    email = ndb.StringProperty()
    photo = ndb.BlobProperty()

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        # 1. Read the request
        current_user = users.get_current_user()
        # 2. Read/write from the database
        people = Person.query().fetch()
        if current_user: #if person is logged in
            current_email = current_user.email()
            current_person = Person.query().filter(Person.email == current_email).get()# the person model who matches the email that logged in
        else:
            current_person = None
        # 3. Render the response
        logout_url = users.create_logout_url("/")
        login_url = users.create_login_url("/")

        templateVars = {
            "people" : people,
            "current_user" : current_user,
            "login_url" : login_url,
            "logout_url" : logout_url,
            "current_person" : current_person,
        }
        template = env.get_template("templates/home.html")
        self.response.write(template.render(templateVars))

class ProfilePage(webapp2.RequestHandler):
    def get(self):
        # 1. Read the request
        urlsafe_key = self.request.get("key") #get from url
        current_user = users.get_current_user()
        # 2. Read/write from the database
        key = ndb.Key(urlsafe=urlsafe_key) # rom url to key
        person = key.get() #from key to person object

        is_my_profile = current_user and current_user.email() == person.email
        # 3. Render the response
        templateVars = {
            "person" : person,
            "is_my_profile" : is_my_profile,
        }
        template = env.get_template("templates/profile.html")
        self.response.write(template.render(templateVars))

class CreateHandler(webapp2.RequestHandler):
    def post(self):
        # 1. Read the request
        name = self.request.get("name")
        biography = self.request.get("biography")
        current_user = users.get_current_user() #step1
        email = current_user.email() #step2
        # 2. Read/write from the database
        person = Person(name=name, biography=biography, email=email)
        person.put()
        # 3. Render the response
        time.sleep(2)#gives it time to render
        self.redirect("/")

class PhotoUploadHandler(webapp2.RequestHandler):
    def post(self):
        image = self.request.get("image")
        current_user = users.get_current_user()
        current_person = Person.query().filter(Person.email == current_user.email()).get()
        current_person.photo
        current_person.put()
        self.redirect("/profile?key=" + current_person.key.urlsafe()) #current person is the person from database, cannot get key from current user

class PhotoHandler(webapp2.RequestHandler):
    def get(self):
        urlsafe_key = self.request.get("key")
        key = ndb.Key(urlsafe=urlsafe_key)
        person = key.get()
        self.response.headers["Content-Type"] = "image/jpg"
        self.response.write(person.photo)

class PotentialRoomies(webapp2.RequestHandler):
    def get(self):
        #1

        #2
        #3
        template = env.get_template("templates/potentialroomies")
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ("/", MainPage),
    ("/profile", ProfilePage),
    ("/create", CreateHandler),
    ("/upload_photo", PhotoUploadHandler),
    ("/photo", PhotoHandler),
    ("/potentialroomies", PotentialRoomies),
], debug=True)
