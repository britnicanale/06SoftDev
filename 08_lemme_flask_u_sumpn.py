from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<!DOCTYPE html><html><head><title>BRITNI CANALE</title></head><body><h1> This is a website that contains some information</h1><p> Hello! This is a website. This website contains some InFORmaTioN. If you are interested in learning more about this information, click <a href =\"morestuff\"> here </a></p></body></html>"

@app.route("/morestuff")
def more_stuff():
    return "<!DOCTYPE html><html><head><title>BRITNI CANALE</title></head><body><h1> This is a website that contains some more information ABOUT the information</h1><p> Hello! Welcome to the information about the information. This information is in regards to the more specific information. It's very important. It's very specific. It contains... information. If you'd like to see the REAL. SPECIFIC. <marquee> INFORMATION. </marquee> click <a href =\"morestuff/specificstuff\"> RIGHT. HERE.</a></p></body></html>"

@app.route("/morestuff/specificstuff")
def specific_stuff():
    return "<!DOCTYPE><html><head><title>DOGE</title></head><body><h1><marquee>DOGE LOL</marquee></h1></body></html>"


if __name__ == "__main__":
    app.debug = True
    app.run()
