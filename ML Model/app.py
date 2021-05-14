from flask import Flask , render_template , request , redirect
import joblib as jb

app = Flask(__name__)

model = jb.load("lin_reg_model.pkl")

@app.route('/')
def display():
	return render_template('index.html')

# send form data/request on same route
@app.route('/' , methods=['POST'])
def marks():

	if request.method == 'POST':
		
		hour = float(request.form['hours'])
		marks = str(model.predict([[hour]])[0][0])

	return render_template('index.html' , your_marks = marks)


if __name__ == '__main__':
	app.run(debug =True)