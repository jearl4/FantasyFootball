# -*- coding: utf-8 -*-

from espnff import League
import datetime
import numpy as np
from flask import Flask, render_template
app = Flask(__name__)

# Logic for web app. Look into breaking this into modules later.
league_id = 646859
year = 2017
league = League(league_id,year)
team1 = league.teams[0]
powerRankings= league.power_rankings(week=2)
topTeamRank = str(powerRankings[0:][1])
topTeamRank = topTeamRank[5:-1]

points= []
teams = []

pRanks = np.asarray(powerRankings)

# Custom date time filter
@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """convert a datetime to a different format"""
    return value.strftime(format)
app.jinja_env.filters['datetimefilter'] = datetimefilter

@app.route("/")
def template_test():
    return render_template('template.html', my_string=team1, my_list=league.teams, title=league.settings.name,
                           current_time=datetime.datetime.now())

@app.route("/home")
def home():
    return render_template('template.html', my_string=team1, my_list=league.teams, title=league.settings.name)

@app.route("/about")
def about():
    return render_template('template.html', my_string=team1, my_list=league.teams, title="About")

@app.route("/contact")
def contact():
    return render_template('template.html', my_string=team1, my_list=league.teams, title="Contact Us")

@app.route("/pRank")
def pRank():
    return render_template('pRank.html', teamArray=teams, pointArray=pRanks, title="Power Rankings")

if __name__ == '__main__':
    app.run(debug=True)