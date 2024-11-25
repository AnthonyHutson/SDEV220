from flask import Flask
app = Flask(__name__)
# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String, unique=True)
    author = db.Column(db.String)
    publisher = db.Column(db.String)

    def __repr__(self):
        return f"{self.book_name} - {self.author}" 



@app.route('/')
def index():
    return 'Hello!'

@app.route('/books')
def get_books():
    return {"books": "book data"}