'''Britni Canale & Dennis Chen
SoftDev1 pd6
K9 -- Solidify
2018-09-20'''

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("about to print __name__...")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":
    app.debug = True
    app.run()
