from flask import Flask , render_template ,  request
app = Flask(__name__)
@app.route ("/")
def index():
    return render_template("index.html")
@app.route("/contact")
def reg():
    return render_template("contact.html")
@app.route ("/about")
def prof():
    return  render_template("about.html")
@app.route("/competition")
def comp():
    return render_template('competition.html')
@app.route("/registration")
def registr():
    return render_template("registration.html")
@app.route ("/profile")
def profile():
    return  render_template("profile.html")
@app.route("/404")
def error404():
    return render_template("404.html")
if __name__ == "__main__":
    app.run(debug=True)