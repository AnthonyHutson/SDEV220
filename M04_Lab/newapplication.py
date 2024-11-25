from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

def app_context():
    app = Flask(__name__)
    with app.app_context():
        yield

app.app_context().push()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String, unique=True)
    author = db.Column(db.String)
    publisher = db.Column(db.String)

    def __repr__(self):
        return f'{self.book_name} - {self.author}'


    @app.route('/')
    def index():
        return 'Hello!'

    @app.route('/books')
    def get_books():

        return {'books': 'book data'}