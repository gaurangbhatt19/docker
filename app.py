from flask import Flask
from redis import Redis


app=Flask(__name__)
redis=Redis(host="redis",port=6379)

@app.route("/")
def flaskapp():
    # key log in redis
    redis.incr("log")
    return 'Flask log: %s' % redis.get("log")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=3333,debug=True)
