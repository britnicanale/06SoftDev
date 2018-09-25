'''MmmmmmChocolate-Britni Canale & Mohammad Uddin
SoftDev1 pd6
K10 -- Jinja Tuning
2018-09-22'''


from flask import Flask, render_template
import util.occupations as occupations


app = Flask(__name__)


#---------FLASK stuff, where the app routes are and the above functions are called---------


@app.route("/")                                 #home route, includes link to occupations route for convenience
def hello_world():
    return "This is the home page<br><a href = \"/occupations\"> Here </a> is a link to a page with information regarding occupations"

@app.route("/occupations")                      #occupations route, contains info regarding some occupations in the US
def hello_temp():
    occs = occupations.getOcc("data/occupations.csv")  #calls function that created dictionary out of the csv file
    return render_template("temp.html", ttl = "Occupations in the United States", rand = occupations.getRandOcc(occs), dict = occs, header = 'Job Class', footer = 'Total')
#                          filename     title of page                             random occupation                    dictionary of occupations 



#----------Where the app is ran-----------
if __name__ == "__main__":
    app.debug = True
    app.run()
