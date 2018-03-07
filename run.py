# This is the entry file for the application
import os
from flask import Flask, render_template

app = Flask(__name__) # Create instance of the Flask class. It is a place holder for the current module

#decorator : 
@app.route('/')
def index():
    # return "<h1>Hello World</h1><h2>This is a Flask Application</h2>"
    return render_template("index.html")
    
@app.route('/about')
def about():
    return render_template("about.html")
    
@app.route('/contact')
def contact():
    return render_template("contact.html")
    
@app.route('/careers')
def careers():
    return render_template("careers.html")
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), # run the server
            port=int(os.environ.get('PORT')),
            debug=True)