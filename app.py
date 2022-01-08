from flask import Flask, render_template, send_from_directory
import os
app = Flask(__name__)

projects = {
    "wizemart":
        {
            "name":"wizemart",
            "link":"www.wizemart.xyz",
            "about":"This is a website that provides a better search experience for shoppers, by scraping and default sorting for the cheapest products from the best rated sellers.",
            "image":"wizemart.jpg",
            "tools":["Flask","Beautifulsoup4","Google-cloud-platform"]
        },
    "holmes":
        {
            "name":"Holmes v1 & 2",
            "link":"github.com/Omoshirokunai/holmes2",
            "about":"A collection of digital image forensics tools brought into an easy to use electron.js GUI",
            "image":"holmes2.png",
            "tools":["Image processing","Streamlit","Digital forensics", "Electron.js"]
        },
    "viz1":
        {
            "name":"Visualization of the programming languages of Github",
            "link":"public.tableau.com/app/profile/hameed.m4525/viz/Githubs-Programming-languages/Dashboard1",
            "about":"Using tableau to visualize programing languages used on github from an aggregated dataset (https://www.kaggle.com/isaacwen/github-programming-languages-data)",
            "image":"viz1.jpg",
            "tools":["Tableau","Data-visualization", "Excel"]
        },
    "jumia-scrape":
        {
            "name":"Jumia scraper",
            "link":"github.com/Omoshirokunai/jumia-index",
            "about":"using beautifulsoup to scrape jumia.com and retrieve a list of products that can be used in web applications like wizemart",
            "image":"jumia-index.png",
            "tools":["web-scraping","beautifulsoup4"]
        },
    "graphics":
        {
            "name":"graphics design work",
            "link":"",
            "about":"A gallery of my past graphics design work including logos, posters.. etc",
            "image":"graphocdesign.webp",
            "tools":["Photoshop","Corel Draw","Gimp","Inkscape"]
        },
        
    "727":
        {
            "name":"727 Softworks",
            "link":"",
            "about":"I am hope to launch a startup idea I've been working on recently, but I've yet to make significant progress on it so employment is currently the priority.",
            "image":"727.webp",
            "tools":["WebRtc","..(Work in progress)"]
        },
}

# ? pages
@app.route("/")
def home():
    return render_template('index.html', title="Home", projects=projects)

@app.route("/gallery")
def gallery():
    return render_template('gallery.html')

@app.route("/resume")
def resume():
    return render_template('resume.html')

@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
# defining function
    return render_template("404.html")

# ? favicon
@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
if __name__ =='__main__':
    app.run(debug=False)