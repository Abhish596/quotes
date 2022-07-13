from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='postgres://qiydziocchtvoh:011981d2d34eb8dbf886a032543969f151ddb9b3f8012b4cc03f59d9c3cd388b@ec2-54-152-28-9.compute-1.amazonaws.com:5432/d5uev0h9nvokq5'
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

