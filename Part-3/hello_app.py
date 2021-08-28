from flask import Flask , jsonify , request , redirect , url_for , render_template

app = Flask(__name__)

# The methods parameter specifies what kind of HTTP requests are allowed for this endpoint. 
# With a POST request, the expectation is that the client application will send data to the web server along with the request.
@app.route('/')
def display():
    return render_template('hello.html')

@app.route('/greet' , methods=['POST'])
def hello():

    # We then call get_json on the request, which gives us the message from the client in JSON. JSON, is a standard way to organize data into key value pairs. 
    # The force=true parameter tells flask to always try to parse the JSON from the request even if its unsure of the datatype.
    message = request.get_json(force = True)

    # We define the name variable to be the value associated with the name key in the JSON data.
    name = message['name']

    # we define a variable called response. This is going to be the response that Flask sends back to the web app. 
    # We set response to a dictionary that contains the key greeting, and the value Hello + name.
    response = {'greeting' : 'Hello, '+name+'!'}
    
    # pass the response to the jsonify function that converts our Python dictionary into JSON. 
    # Our hello function then returns this JSON response to the web application.
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug = True)
