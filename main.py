import webapp2
import jinja2
import os
import logging
import time

from google.appengine.ext import ndb
from google.appengine.api import users

class Person(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    gender = ndb.StringProperty()
    college = ndb.StringProperty()
    year = ndb.StringProperty()
    city = ndb.StringProperty()
    state = ndb.StringProperty()
    bio = ndb.StringProperty()
    photo = ndb.BlobProperty()

class Like(ndb.Model):
    liker_key = ndb.KeyProperty()
    liked_key = ndb.KeyProperty()

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
        if current_user: #if person exists
            current_email = current_user.email()
            current_person = Person.query().filter(Person.email == current_email).get()# the person model who matches the email that logged in
        else:
            current_person = None
        # 3. Render the response
        logout_url = users.create_logout_url("/")
        #print(repr(current_person))
        #print(repr(people))
        if current_person:
            #print("took true branch")
            login_url = users.create_login_url("/")
        else:
            #print("took false branch")
            login_url = users.create_login_url("/")
        print(login_url)
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
        urlsafe_profile_key = self.request.get("key") #get from url
        current_user = users.get_current_user()
        current_person = Person.query().filter(Person.email == current_user.email()).get()
        # 2. Read/write from the database
        key = ndb.Key(urlsafe=urlsafe_profile_key) # rom url to key
        viewed_person = key.get() #from key to person object

        is_my_profile = current_user and current_user.email() == viewed_person.email
        # 3. Render the response
        templateVars = {
            "current_person" : current_person,
            "person" : viewed_person,
            "is_my_profile" : is_my_profile,
        }
        template = env.get_template("templates/profile.html")
        self.response.write(template.render(templateVars))

    def post(self):
        #1
        #urlsafe_key = self.request.get("") #main issue
        current_user = users.get_current_user()
        current_person = Person.query().filter(Person.email == current_user.email()).get()

        #key = ndb.Key(urlsafe=urlsafe_key) # rom url to key
        viewed_profile_key = self.request.get("viewed_profile_key") #this is the urlsafe key gettingreturned
        key = ndb.Key(urlsafe=viewed_profile_key)
        viewed_profile = key.get()

        #2
        like = Like(liker_key = current_person.key, liked_key = viewed_profile.key)
        like.put()
        #3
        time.sleep(2)
        self.redirect("/profile?key=" + viewed_profile.key.urlsafe())

class CreateHandler(webapp2.RequestHandler):
    def post(self):
        # 1. Read the request
        name = self.request.get("name")
        gender = self.request.get("gender")
        college = self.request.get("college")
        year = self.request.get("year")
        city = self.request.get("city")
        state = self.request.get("state")
        bio = self.request.get("bio")
        current_user = users.get_current_user() #step1
        email = current_user.email() #step2

        # 2. Read/write from the database
        person = Person(name=name, gender=gender, college=college, year=year, city=city, state=state, bio=bio, email=email)
        person.put()
        # 3. Render the response
        time.sleep(2)#gives it time to render
        self.redirect("/potentialroomies")

class EditHandler(webapp2.RequestHandler):
    def post(self):
        current_user = users.get_current_user()
        current_person = Person.query().filter(Person.email == current_user.email()).get()
        person = Person.query().filter(Person.email == current_user.email()).get()
        name = self.request.get("name")
        gender = self.request.get("gender")
        college = self.request.get("college")
        year = self.request.get("year")
        city = self.request.get("city")
        state = self.request.get("state")
        bio = self.request.get("bio")

        person.name = name
        person.gender = gender
        person.college = college
        person.year = year
        person.city = city
        person.state = state
        person.bio = bio
        person.put()
        time.sleep(2)
        self.redirect("/profile?key=" + current_person.key.urlsafe())

class PhotoUploadHandler(webapp2.RequestHandler):
    def post(self):
        image = self.request.get("image")
        current_user = users.get_current_user()
        current_person = Person.query().filter(Person.email == current_user.email()).get()
        current_person.photo = image
        current_person.put()
        time.sleep(2)
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
        current_user = users.get_current_user()
        current_person = Person.query().filter(Person.email == current_user.email()).get()
        logging.info(current_person)
        #2
        people = Person.query().filter(Person.gender == current_person.gender)
        people = people.filter(Person.college == current_person.college)
        people = people.filter(Person.year == current_person.year)
        #people = people.remove(Person.email == current_user.email())
        #3
        templateVars = {
            "current_person" : current_person,
            "people" : people,
        }
        template = env.get_template("templates/potentialroomies.html")
        self.response.write(template.render(templateVars))

class MyMatches(webapp2.RequestHandler):
    def get(self):
        #1
        current_user = users.get_current_user()
        current_person = Person.query().filter(Person.email == current_user.email()).get()
        #2

        #3
        templateVars = {
            "current_person" : current_person,
        }
        template = env.get_template("templates/mymatches.html")
        self.response.write(template.render(templateVars))

app = webapp2.WSGIApplication([
    ("/", MainPage),
    ("/profile", ProfilePage),
    ("/create", CreateHandler),
    ("/edit", EditHandler),
    ("/upload_photo", PhotoUploadHandler),
    ("/photo", PhotoHandler),
    ("/potentialroomies", PotentialRoomies),
    ("/mymatches", MyMatches)
], debug=True)
