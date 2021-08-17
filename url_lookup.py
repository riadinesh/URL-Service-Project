from enum import unique
from sqlalchemy.sql.schema import UniqueConstraint
import validators

from flask import Flask, request, redirect, url_for, render_template, session, flash
#allows for a redirect from a specific function
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'project'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///table.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db =SQLAlchemy(app)

class links(db.Model):
    #add columnns for table
    #length of string = 100 characters max
    #link = db.Column(db.String(100), primary_key = False, unique = False)
    link = db.Column(db.String(100), primary_key = True, nullable = False)

    def __init__(self, link):
        self.link = link

    def __str__ (self):
        return '{self.link}'.format(self=self)

        
@app.route("/home")
def initial_route():   
    return render_template("welcome.html", 
    message1 = "http://127.0.0.1:5000/url_name=www.google.com")


@app.route("/add", methods=["POST", "GET"])
def add_db():
    url = None
    if request.method == "POST":
        url = request.form["url"]
        found_link = links.query.filter_by(link = url).first()

        try:
            link1 = links(url)
            db.session.add(link1)
            db.session.commit()
            print(links.query.all())
            flash("URL added to malware database.", "info")
            url = None
        except:
            flash("This URL is already in database. Enter another URL.", "info")
            url = None

    return render_template("add_url.html", url = url)

@app.route("/display")
def print_all():
    query_list = links.query.all()
    for entry in query_list:
        str_entry = str(entry)
        flash(str_entry)
        #return render_template("print_all.html", str_entry = str_entry)
    return render_template("print_all.html")

@app.route("/url_name")
def validate():
    #gets the value of the key "url" and sets it to val
    val = request.args.get("url")
    valid = validators.url(val)

    #url is valid so now you can check if it is malware
    if valid:       
        malware_link = links.query.filter_by(link = val).first()
        if malware_link:
            return render_template("index.html", content = val, is_safe = False)  
        return render_template("index.html", content = val, is_safe = True)  
    else:
        return render_template("index.html", content = val, valid = False)  



if __name__ == "__main__":
    db.create_all()
    app.run(host = '0.0.0.0', port=5000, debug=True)


