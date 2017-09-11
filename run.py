# -*- coding: utf-8 -*-

from espnff import League
from flask import Flask, render_template
app = Flask(__name__)

league_id = 646859
year = 2017
league = League(league_id,year)
team1 = league.teams[4]


@app.route("/")
def template_test():
    return render_template('template.html', my_string=team1, my_list=league.teams, title="Home")

@app.route("/home")
def home():
    return render_template('template.html', my_string=team1, my_list=league.teams, title="Home")

@app.route("/about")
def about():
    return render_template('template.html', my_string=team1, my_list=league.teams, title="About")

@app.route("/contact")
def contact():
    return render_template('template.html', my_string=team1, my_list=league.teams, title="Contact Us")

@app.route("/pRank")
def pRank():
    return render_template('template.html', my_string=team1, my_list=league.power_rankings(week=1), title="Power Rankings")

if __name__ == '__main__':
    app.run(debug=True)