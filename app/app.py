
import os
from flask import Flask, render_template, redirect, url_for
from app import app, db
from app.forms import ManagerTeamForm
from app.models import Manager, Team, ManagerTeam


@app.route('/', methods=['GET','POST'])
def index():
  return render_template('index.html')


@app.route('/demo', methods=['GET','POST'])
def demo():
  return render_template('app/demo_queries/templates/demo.html')


@app.route('/form', methods=['GET','POST'])
def mtform():
  mtform = ManagerTeamForm()
  if mtform.validate_on_submit():
    new_manager = Manager(
                manager_name = mtform.manager_name.data
                )
    new_team = Team(
                team_name = mtform.team.data 
                )
    new_managerteam = ManagerTeam(
                start_date = mtform.start_date.data,
                end_date = mtform.end_date.data 
                )

    # Save game method
    new_manager.save_manager() 
    new_team.save_team()
    new_managerteam.save_managerteam()
    
    return redirect(url_for('index'))
      
  return render_template('page.html', form = mtform)


if __name__ == '__main__':
    app.run(debug=True)
    