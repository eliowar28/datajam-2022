from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def home_view():
        return "<h1>DataJAM 2022!! deploy test new test</h1>"