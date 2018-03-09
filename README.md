# Thorin and Company

A tutorial using Python and Flask to develop the back end of a website.
At the moment it stores information in a json file.

## Things covered

* fundamentals of using Flask
* routing using decorations
* render from templates
* different request methods, GET and POST
* using flash for giving feedback to users.

**requirements.txt** file is a file that Python projects use to handle 
dependency management.

**Procfile** is a heroku-specific file that tells heroku that this is a web 
application and that we will use the run.py command to run it.

* * *
Another error:  
**“No web processes running”**

We're telling heroku we want to use a web process but we're not actually 
starting any web processes. This is basically just a watcher that will sit and 
watch our file that we're running continuously so that it makes any changes. 
We need to run the following command in the command-line in cloud 9.

~~~~
heroku ps:scale web=1
~~~~

Then go to heroku's *settings* and press on **Reveal Config Vars**. Here you 
need to create some config vars. Set the following key : values: 

**IP**|**0.0.0.0**
:--|--
**PORT**|**5000**

We need to set these as we are reading them from the environment variables in 
**run.py**  
We are using this code:

~~~~python
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), # run the server
            port=int(os.environ.get('PORT')),
            debug=True)
~~~~


If we don't specify them here then the application won't actually be able to 
find them and run them which will lead to us getting errors that say that we 
can't run the application. 

Go to **More** in Heroku and **restart all dynos**.  
The **dynos** are just **containers that our code is running in**.
