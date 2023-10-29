from flask import *

#last search
search_history = []

app = Flask(__name__)

#search
@app.route("/")
def index():
    return render_template('index.html', search_history=search_history)

@app.route("/submit", methods=["POST"])
def submit():
    key = ""
    key = request.form["search"]
    search_history.append(key)
    return redirect("https://www.google.com/search?q=" + key)

#about page
@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
