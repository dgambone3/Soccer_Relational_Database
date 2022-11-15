
import psycopg2
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from app.forms import ManagerTeamForm
from models import Manager, Team, ManagerTeam


# create the extension
db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://wpepkodmgckzze:02be78245346d6bc03fa4e5e667e3904529f762923b9ce6f3c5527cbf06c5858@ec2-34-230-153-41.compute-1.amazonaws.com:5432/d79mtf79npaf4h'
db.init_app(app)

@app.route('/')
def hello():
  
  form = ManagerTeamForm()
  if form.validate_on_submit():
    new_manager = Manager(
                manager_name = form.manager_name.data
                )
    new_team = Team(
                team_name = form.team.data 
                )
    new_managerteam = ManagerTeam(
                start_date = form.start_date.data,
                end_date = form.end_date.data 
                )

    # Save game method
    new_manager.save_manager() # TODO: write save methods for each model.
    new_team.save_team()
    new_managerteam.save_mt()
      
  return render_template('page.html')


if __name__ == '__main__':
    app.run(debug=True)
    