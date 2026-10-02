from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/forecast")
def forecast():
    return render_template("forecast.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/reports")
def reports():
    return render_template("reports.html")


@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/locations")
def locations():
    return render_template("locations.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

if __name__ == "__main__":
    app.run(debug=True)