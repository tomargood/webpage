import requests
from datetime import datetime as dt, timezone
from flask import Flask, render_template, redirect, request, url_for, flash



app = Flask(__name__)
app.secret_key = 'dev'

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/wxchecker")
def wxchecker():
    return render_template("wxchecker.html")

@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")

@app.route("/dashboards")
def dashboards():
    return render_template("dashboards.html")

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == "POST":
        if not request.form.get('arpt'): 
            return render_template("wxchecker.html", show_modal=True) # Redirect back to the form page
        else:
            arpt = request.form['arpt']
            return redirect(url_for('result', arpt=arpt))


@app.route("/<arpt>")
def result(arpt):
    if lookup(arpt)==None:
        return render_template("wxchecker.html", show_modal=True)
    else:
        vis, cig, time, full_name, cover, type, color = lookup(arpt)
        return render_template("result.html", full_name=full_name, arpt=arpt, vis=vis, cig=cig, time=time, cover=cover, type=type, color=color)


def lookup(arpt):
    try:
        response = requests.get(f"https://aviationweather.gov/api/data/metar?ids={arpt}&format=json")
        my_dict = response.json()
        vis = my_dict[0]["visib"]
        if cigcalc(my_dict[0]["clouds"]) is not None:
            cig = cigcalc(my_dict[0]["clouds"])['base']
            cover = cigcalc(my_dict[0]["clouds"])["cover"]
        else:
            cig = my_dict[0]["clouds"][0]['base']
            cover = my_dict[0]["clouds"][0]["cover"]
        time = my_dict[0]["reportTime"]
        full_name=my_dict[0]["name"]
        type = wxtype(cig,vis,cover)
        color = wxtypecolor(type)
        return vis, cig, time, full_name, cover, type, color
    except:
        return None


def wxtype(cig,vis,cover):
    if vis == "10+":
        vis = 10
    if cig is None:
        cig = 10000000
    if int(cig) > 3000 and int(vis) > 5:
        type = "VFR"
    elif int(cig) > 1000 and int(vis) > 3:
        type = "MVFR"
    elif int(cig) >= 500 and int(vis) >= 1:
        type = "IFR"
    elif int(cig) < 500 or int(vis) < 1:
        type = "LIFR"
    else:
        type = "Unknown"
    return type

def wxtypecolor(type):
    if type == "VFR":
        color = "table-success"
    elif type == "MVFR":
        color = "table-primary"
    elif type == "IFR" or type == "LIFR":
        color = "table-danger"
    else: color="table-danger"
    return color

def cigcalc(clouds):
        for each in clouds:
            if each["cover"] == "BKN" or each["cover"] == "OVC":
                return each


if __name__ == "__main__":
    app.run(host="0.0.0.0")
