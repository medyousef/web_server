from flask import Flask
app=Flask(__name__)

#routes
@app.route("/")
def index():
    return "hello from flask"
app.run(host="0.0.0.0")
