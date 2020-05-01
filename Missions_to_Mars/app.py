

# Route to render index.html template using data from Mongo

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


@app.route("/")
def index():

    mars = mongo.db.mars.find_one()
    # Return template and data
    return render_template("index.html", mars_scraping_data =mars)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    mars = mongo.db.mars()
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data, upsert = True)
    

    # Redirect back to home page
    return redirect("//localhost:5000/", code = 302)


if __name__ == "__main__":
    app.run(debug=True)
