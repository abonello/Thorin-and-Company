# This is the entry file for the application
import os
import json
from flask import Flask, render_template

app = Flask(__name__) # Create instance of the Flask class. It is a place holder for the current module

#decorator : 
@app.route('/')
def index():
    # return "<h1>Hello World</h1><h2>This is a Flask Application</h2>"
    return render_template("index.html", page_title="Home Page")
    
@app.route('/about')
def about():
    data = []
    with open('data/company.json', 'r') as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company_data = data)

@app.route('/about/<member_name>')
def about_member(member_name):
    member = {}
    with open('data/company.json', 'r') as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj['url'] == member_name:
                member = obj
    
    # return "<h1>" + member["name"] + "</h1>"
    return render_template("member.html", member=member)
    

@app.route('/contact')
def contact():
    return render_template("contact.html", page_title="Contact")
    
@app.route('/careers')
def careers():
    return render_template("careers.html", page_title="Vacancies", subtitle="Come work with us!")
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), # run the server
            port=int(os.environ.get('PORT')),
            debug=True)