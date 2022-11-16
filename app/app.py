
import psycopg2
import os
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from forms import ManagerTeamForm


# create the db instance

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')

db = SQLAlchemy(app)
db.init_app(app)

class Manager(db.Model):
    __tablename__ = 'manager'

    manager_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    manager_name = db.Column(db.VARCHAR(length=50))
    
    def save_manager(self):
        db.session.add(self)
        db.session.commit()

class Team(db.Model):
    __tablename__ = 'team'

    team_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    venue_id = db.Column(db.Integer)
    team_name = db.Column(db.VARCHAR(length=50))
    
    def save_team(self):
        db.session.add(self)
        db.session.commit()

class ManagerTeam(db.Model):
    __tablename__ = 'managerteam'
    
    contract_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    manager_id = db.Column('manager_id', db.ForeignKey('manager.manager_id'),nullable=False)
    team_id = db.Column('team_id', db.ForeignKey('team.team_id'),nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=True)
    
    def save_managerteam(self):
        db.session.add(self)
        db.session.commit()



@app.route('/', methods=['GET','POST'])
def index():
  return render_template('index.html')

@app.route('/demo', methods=['GET','POST'])
def demo():
  return render_template('demo.html')

@app.route('/form', methods=['GET','POST'])
def mtform():
  mtform = ManagerTeamForm()
  # if mtform.validate_on_submit():
  if request.method == 'POST':
    # last_m_id = db.session.execute(db.select(Manager.manager_id).order_by(Manager.manager_id))
    last_m_id = db.session.execute(db.select(func.max(Manager.manager_id))).scalar()
    new_m_id = last_m_id + 1
    last_t_id = db.session.execute(db.select(func.max(Team.team_id))).scalar()
    new_t_id = last_t_id + 1
    last_mt_id = db.session.execute(db.select(func.max(ManagerTeam.contract_id))).scalar()
    new_mt_id = last_mt_id + 1
    new_manager = Manager(
                manager_id = new_m_id,
                manager_name = mtform.manager_name.data
                )
    new_team = Team(
                team_id = new_t_id,
                team_name = mtform.team.data 
                )
    new_managerteam = ManagerTeam(
                contract_id = new_mt_id,
                manager_id = new_m_id,
                team_id = new_t_id,
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
    