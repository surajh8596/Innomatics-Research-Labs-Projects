from flask import Flask, url_for, render_template, redirect, request
import pyshorteners
import validators
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app=Flask(__name__)

#SQLAlchemy Configuration and pass the application into SQLAlchemy class
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)
Migrate(app, db)

#Create a Model or Table
class URL_Shortner(db.Model):
    __tablename__='short_urls'
    id = db.Column(db.Integer, primary_key = True)
    org_url = db.Column(db.Text)
    title = db.Column(db.Text)
    short_url= db.Column(db.Text)

    def __init__(self, org_url, title, short_url):
        self.org_url = org_url
        self.title = title
        self.short_url=short_url

    def __repr__(self):
        return f"<URL_Shortner {self.org_url}>"



@app.route('/')
def home():
    return render_template('layout.html')

@app.route('/short_url', methods=['POST', 'GET'])
def short_url():
    if request.method=='POST':
        url=request.form.get('url')
        title=request.form.get('title')
        is_url=validators.url(url)
        if is_url:
            s=pyshorteners.Shortener()
            short_url=s.tinyurl.short(url)
            short_url=short_url.replace("https://", "")

            new_url=URL_Shortner(url, title, short_url)
            db.session.add(new_url)
            db.session.commit()
            return render_template('short_url.html', url=url, title=title, short_url=short_url, is_url=is_url)
        return render_template('short_url.html', is_url=is_url)
    return render_template('short_url.html')

@app.route('/search')
def search():
    url=request.args.get("url")
    urls=URL_Shortner.query.filter_by(org_url=url).first()
    return render_template('search.html', urls=urls)


@app.route('/history')
def history():
    all_url=URL_Shortner.query.all()
    return render_template('history.html', all_url=all_url)


if __name__=='__main__':
    app.run(debug=True)