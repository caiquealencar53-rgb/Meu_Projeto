from flask import Flask

app = Flask(__name__)
@app.route("/")
def homepage():
    return "que cheiro de makonia"
if __name__=="__main__":
    app.run(debug=True)