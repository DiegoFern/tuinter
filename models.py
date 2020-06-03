from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
"""Construct the core application."""
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


def create_app():
    db.create_all()  # Create database tables for our data models


Model = db.Model


class User(Model):
    __tablename__ = 'User'
    Name = db.Column(db.String)
    Password = db.Column(db.String)
    Email = db.Column(db.String, primary_key=True)
    message = db.relationship('Message',backref='User')

    following = db.relationship(
            'User', lambda: Follow_table,
            primaryjoin=lambda: User.Email == Follow_table.c.left_id,
            secondaryjoin=lambda: User.Email == Follow_table.c.right_id,
            backref='Follow'
        )

    @staticmethod
    def Valid(Name, Password):
        return User.filter(Name=Name, Password=Password).exists()

    def json(self):
        return {'email':(self.Email), 'name':(self.Name)}

class Message(Model):
    __tablename__ = 'Message'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    text = db.Column(db.String)
    editor = db.Column(db.String,db.ForeignKey('User.Email'))

Follow_table = db.Table( 'Follow',
    db.Column('left_id', db.Integer, db.ForeignKey('User.Email')),
    db.Column('right_id', db.Integer, db.ForeignKey('User.Email'))
)


if __name__ == '__main__':
    print('creating')
    create_app()
