# This is the entry file for the application
import os
from flask import Flask, render_template

app = Flask(__name__) # Create instance of the Flask class. It is a place holder for the current module

#decorator : 
@app.route('/')
def index():
    # return "<h1>Hello World</h1><h2>This is a Flask Application</h2>"
    return render_template("index.html", page_title="Home Page")
    
@app.route('/about')
def about():
    return render_template("about.html", page_title="About", list_of_numbers=["Line 1", "Line 2", "Line 3"])
    
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