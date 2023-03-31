# All of the Flask related activities and Whole app will be executed from this file. 
# It's a heart of our project. 

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

