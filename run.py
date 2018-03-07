# This is the entry file for the application
import os
from flask import Flask

app = Flask(__name__) # Create instance of Flask

#decorator : 
@app.route('/')
def hello():
    return "Hello World"
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), # run the server
            port=int(os.environ.get('PORT')),
            debug=True)