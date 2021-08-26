### Integrate HTML With Flask
### HTTP verb GET And POST

from flask import Flask , render_template , request , redirect , url_for

app = Flask(__name__)


@app.route('/')
def display():
    return render_template('index.html')


@app.route('/success/<int:marks>')
def success(marks):
    res = 'PASS'
    return render_template('result.html' , result = res , score = marks)


@app.route('/fail/<int:marks>')
def fail(marks):
    res = 'FAIL'
    return render_template('result.html' , result = res , score = marks)


@app.route('/submit' , methods = ['GET' , 'POST'])
def results():
    total_score = 0
    if request.method == 'POST':
        math = float(request.form['maths'])
        science = float(request.form['science'])
        c = float(request.form['c'])
        ds = float(request.form['datascience'])
        total_score = (math+science+c+ds)/4

    if total_score>50:
        res = 'success'
    else:
        res = 'fail'

    return redirect(url_for(res , marks = total_score))


if __name__=="__main__":
    app.run(debug = True)