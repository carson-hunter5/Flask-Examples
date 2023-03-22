# 02-HelloWorld Example 

# import the Flask library
from flask import Flask

# create a Flask object using the name of the current module, 
# which will be '__main__'
app = Flask(__name__)

# Defining a new handler function for the route `GET /`. 
# The default method (verb) is GET, so you don't have to 
# explicitly include it as I have done here. 
@app.route("/", methods=['GET'])
def hello_world():
    return "<h1>Hello CS 3200</h1>"

if __name__ == '__main__':
    # `debug = True` -> runs the app in debug mode 
    #    which allows for hot reloading of code(for hot reloading) 
    # `port = 4000` -> indicates what network port this app will be
    #    bound to... in this case, port 4000. 
    app.run(debug = True, port = 4000)