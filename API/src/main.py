from flask import Flask, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from random import randint
from faker import Faker
from random import randint
fake=Faker()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://root:root@localhost:5432/contacts"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


@app.route("/user", methods = ["POST", "GET"])


class contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(200))
    firstname = db.Column(db.String(200))
    lastname = db.Column(db.String(200))
    email = db.Column(db.String(200))


def __init__(self, number, firstname, lastname, email):
    self.number = number
    self.firstname = firstname
    self.lastname = lastname
    self.email = email

def contact_tables():
    for i in range(0,100):
        #création des fausses
        new_user = users(fake.first_name(),fake.last_name(),randint(20,60), fake.email(), fake.job())
        apps=["facebook","twitter","instagram","snapchat","linkdin"]
        nb_app = 2 #random choice 1, 2, 3, 4, 5
        applications = []
        for app_n in range(0, nb_app):
            app= Application(apps[app_n], fake.user_name(), datetime.now())
            applications.append(app)
        new_user.applications=applications
        db.session.add(new_user)
    db.session.commit()


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(host="0.0.0.0", port=8080, debug=True)
