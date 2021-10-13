from flask import Flask

app=Flask(__name__)

@app.route("/")
def flaskapp():
    return "Flask"

if __name__=="__main__":
    app.run(port=3030,debug=True)