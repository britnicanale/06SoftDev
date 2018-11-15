
from flask import Flask, render_template
import json, urllib


app = Flask(__name__)


url = "https://api.getchute.com/v2"

@app.route("/")
def hello():

    url = "https://api.getchute.com/v2"

    username = "username"
    password = "password"
    values = """
      {
        "urls": [
          "https://media.getchute.com/media/1EEangu"
        ],
        "user_info": {
          "name": "name",
          "username": "username",
          "profile": {
            "First Name": "UserFirstName"
          }
        }
      }
    """


    values = values.encode('utf-8')

    headers = {
      'Content-Type': 'application/json'
    }
    request = urllib.request.Request('https://api.getchute.com/v2/albums/{album}/assets/import?urls=&shortcuts=&instagram_ids=&oauth_token=', data=values, headers=headers)

    response_body = urllib.request.urlopen(request).read()
    print (response_body)

    return render_template("index.html")

if __name__== "__main__":
    app.debug = True
    app.run()
