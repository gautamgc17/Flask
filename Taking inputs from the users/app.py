from flask import Flask , render_template , redirect , request
app = Flask(__name__)

friends_list = ['gautam' , 'parth' , 'sanjay']  
count = 3 

@app.route('/')   
def display():
	return render_template('index.html' , my_friends = friends_list , number = count)   
@app.route('/about')
def about():
	return 'This is about page'



@app.route('/submit' , methods = ['POST'])  # By default, a route only answers to GET requests. Use the methods argument of the route() decorator to handle different HTTP methods.
def submit_form():

	if request.method == 'POST':
		name = request.form['username']    # returns a Dictionary object which contains the key-value pair of form parameters and their values
		age = int(request.form['age'])

		file_content = request.files['userfile']
		file_content.save(file_content.filename)     # name of the target file same as uploaded by user

	return "<h3> Hello {}!! Your age is: {}".format(name , age)



if __name__ =='__main__':
	app.run(debug = True)