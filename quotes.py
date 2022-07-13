from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='postgres://kxzvazhdzahudz:4d15e33a5c93811fa93b8230dccc5dfd65dde8198eb1af16e14a791b8519ae25@ec2-54-87-179-4.compute-1.amazonaws.com:5432/d9g5vkqm69u4e4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Quote(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(200), nullable=False)
    quote = db.Column(db.String(2000), nullable=False)


@app.route("/")
def home():
    result = Quote.query.all()
    return render_template("index.html",result=result)


@app.route('/add', methods=['GET','POST'])
def add_quote():
    if request.method == "POST":
        author = request.form['author']
        quote = request.form['quote']
        new_data = Quote(author=author, quote=quote)
        db.session.add(new_data)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("quotes.html")

