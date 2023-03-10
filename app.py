from flask import Flask

app = Flask(__name__)
# __name__ is the placeholder for the current module (App.py)

@app.route('/')
def index():
    return 'Hello   World'

if __name__ == '__main__':
    # script which will be executed
    app.run(debug=True)
    # allows us to start running the application
    # pass debug = True to run() to enable debug mode. 
    # this way you can see your code changes without having to contantly restart the server