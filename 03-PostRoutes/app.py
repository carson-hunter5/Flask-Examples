# 02-SimpleRoutes Example

# import the Flask framework
from flask import Flask, request, render_template

# create a flask object
app = Flask(__name__)

# Defining a new handler function for the route `GET /`. 
# The default method (verb) is GET, so you don't have to 
# explicitly include it as I have done here.  
@app.route("/", methods=['GET'])
def hello_world():
    return "<h1>Hello CS 3200</h1>"

# this route will handle the user going to /bigHello
# It returns a different string and with the H1 html tag
# Note, without the methods parameter, it is assumed to be 
# a GET route.
@app.route("/bigHello", methods=['GET'])
def big_hello_world():
    return "<h1>A Big Hello to you!!!!</h1>"

# Route handler for GET /users/<idNumber>
# idNumber is a variable in the URL / endpoint. 
# we can access the variable in the function handler using 
# curly braces. 
@app.route("/users/<idNumber>", methods=['GET'])
def handle_user_with_id(idNumber):
    return f'<h2>You asked for {idNumber} id.'

@app.route("/userForm", methods=['GET'])
def get_user_form():
    return render_template('postHome.html')

# Route for POSTing to /products 
@app.route("/userInfo", methods=['POST'])
def handle_new_product():
    print(request.json)
    return {"message":"Success"}

# If this file is being run directly, then run the application 
# via the app object. 
# debug = True will provide helpful debugging information and 
#   allow hot reloading of the source code as you make edits and 
#   save the files. 
# port = 4000 binds this to network port 4000
if __name__ == '__main__': 
    app.run(debug = True, port = 4000)