from flask import Flask, render_template

app = Flask(__name__)
# __name__ is the placeholder for the current module (App.py)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    # script which will be executed
    app.run(debug=True)
    # allows us to start running the application
    # pass debug = True to run() to enable debug mode. 
    # this way you can see your code changes without having to contantly restart the server