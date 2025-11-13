
from flask import Flask, render_template
from main_scraper import scrape_main_page

app = Flask(__name__)

@app.route('/')
def home():

    data = scrape_main_page()  # scrape one listing
   
    return render_template('listing.html', items=data)


if __name__ == '__main__':
    app.run(debug=False)
