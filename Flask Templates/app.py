from flask import Flask , render_template , redirect
app = Flask(__name__)

friends_list = ['gautam' , 'parth' , 'sanjay']  
count = 3 

@app.route('/')   
def display():
	return render_template('index.html' , my_friends = friends_list , number = count)   # render_template is used to generate output from a template file based on the Jinja2 engine that is found in the application's templates folder

@app.route('/about')
def about():
	return 'This is about page'

@app.route('/home')
def return_display():
	return redirect('/')     # When called, it returns a response object and redirects the user to another target location (here it redirects to '/' route)

if __name__ =='__main__':
	app.run(debug = True)