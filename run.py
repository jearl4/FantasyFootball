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
    return render_template('template.html', my_string=team1, my_list=league.teams)


if __name__ == '__main__':
    app.run(debug=True)