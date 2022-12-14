#first server where i leared how to perform get, post, 
#put and delete requests.
#https://www.youtube.com/watch?v=msEmUtYqVV0 this is the
#tutorial I followed I hav not completed the react portion 
#as i feel my react knowledge is up to date

import json
from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_marshmallow import Marshmallow


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Gerry2482@localhost/pyflask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text())
    date = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self,title,body):
        self.title = title
        self.body = body
        

class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id','title','body', 'date')

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)


@app.route("/login", methods = ['GET'])
def login():
    username = "gerrydeemo"
    password = "Gerry2482"
    payload = (username, password)
    return jsonify(payload)

@app.route("/get", methods = ['GET'])
def get_articles():
    all_articles = Articles.query.all()
    results = articles_schema.dump(all_articles)
    return jsonify(results)

@app.route("/get/<id>/", methods = ['GET'])
def post_details(id):
    article = Articles.query.get(id)
    return article_schema.jsonify(article)

@app.route("/delete/<id>/", methods = ['DELETE'])
def delete_post(id):
    article = Articles.query.get(id)
    db.session.delete(article)
    db.session.commit()
    return article_schema.jsonify(article) 


@app.route("/post", methods = ['POST']) 
def add_article():
    title = request.json['title']
    body = request.json['body']
    articles = Articles(title,body)
    db.session.add(articles)
    db.session.commit()
    return article_schema.jsonify(articles)

@app.route("/update/<id>/", methods = ['PUT'])
def update_article(id):
    article = Articles.query.get(id)

    title = request.json['title']
    body = request.json['body']

    article.title = title
    article.body = body

    db.session.commit()
    return article_schema.jsonify(article)

if __name__ == "__main__":
    app.run(debug=True)