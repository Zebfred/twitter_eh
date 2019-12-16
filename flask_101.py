"flask 101"

from flask import Flask

#applationi

app = Flask(__name__)

#route
@app.route("/")

#function
def hello():
    return  "Hello World!"

if __name__ == "__main__":
  app.run()