# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask app
app = Flask(__name__)

# Configure the database URI (SQLite in this example)

# Initialize the database

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/about.html', methods=['GET', 'POST'])
def about():
    if request.method == ("GET"):
        return render_template('about.html')
    
@app.route('/links.html', methods=['GET', 'POST'])
def link():
    if request.method == ("GET"):
        return render_template('links.html')
    


if __name__ == '__main__':
    app.run(debug=True)