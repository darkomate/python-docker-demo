from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome Home to Docker!</h1><br /><h3>Python is here!</h3>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8003)