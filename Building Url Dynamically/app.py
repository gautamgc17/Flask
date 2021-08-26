## Variable Rules and URL Building
from flask import Flask , request , render_template , redirect , url_for

app = Flask(__name__)

## decorator that binds a url with function
@app.route('/')
def welcome():
    return 'Welcome to Flask Practice'


## flask route params - parameters can be used when creating routes
@app.route('/pass/<int:score>')
def success(score):
    return "The person has passed and marks scored are: " + str(score)


@app.route('/fail/<score>')
def fail(score):
    return "The person has failed and marks scored are: " + score


## flask route with multiple arguments
@app.route('/name/<first_name>/<last_name>')
def name(first_name=None , last_name=None):
    return "Name is "+first_name+" Last Name is "+last_name


## build url for function and redirecting
@app.route('/results/<int:marks>')
def results(marks):
    if marks < 50:
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result , score = marks))   # pass function name and optionally its keyword arguments


if __name__=="__main__":
    app.run(debug=True)