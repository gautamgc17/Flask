from flask import Flask
app = Flask(__name__)   # create object of Flask class ; This is the WSGI application

@app.route('/')    # decorator which tells the application which URL should call the associated function responsible for returning the server response
def display():
	return "This is our first Flask application😉✌"

@app.route('/new')        # different routes with different binding functions
def new():
	return 'This is another web page!!'

if __name__ =='__main__':
	app.run(debug = True)
