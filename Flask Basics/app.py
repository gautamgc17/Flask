from flask import Flask
app = Flask(__name__)   # object of Flask class is our WSGI application

@app.route('/')   # decorator which tells the application which URL should call the associated function responsible for returning the server response
def display():
	return "This is our first Flask application😉✌"

if __name__ =='__main__':
	app.run(debug = True)