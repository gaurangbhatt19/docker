from flask import Flask

app=Flask(__name__)

@app.route("/")
def flaskapp():
    return "Flask"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=3333,debug=True)
