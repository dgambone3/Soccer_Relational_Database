
import psycopg2
import os
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from app.forms import ManagerTeamForm


# create the extension
db = SQLAlchemy()
class Manager(db.Model):
    __tablename__ = 'manager'

    manager_id = db.Column(db.Integer, primary_key=True)
    manager_name = db.Column(db.VARCHAR(length=50))
    
    def save_manager(self):
        db.session.add(self)
        db.session.commit()

class Team(db.Model):
    __tablename__ = 'team'

    team_id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer)
    team_name = db.Column(db.VARCHAR(length=50))
    
    def save_team(self):
        db.session.add(self)
        db.session.commit()

class ManagerTeam(db.Model):
    __tablename__ = 'managerteam'
    
    contract_id = db.Column(db.Integer, primary_key=True)
    manager_id = db.Column('Manager', db.ForeignKey('manager.manager_id'))
    team_id = db.Column('Team', db.ForeignKey('team.team_id'))
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=True)
    
    def save_managerteam(self):
        db.session.add(self)
        db.session.commit()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://wpepkodmgckzze:02be78245346d6bc03fa4e5e667e3904529f762923b9ce6f3c5527cbf06c5858@ec2-34-230-153-41.compute-1.amazonaws.com:5432/d79mtf79npaf4h'
app.secret_key = os.environ.get('SECRET_KEY', 'dev')
db.init_app(app)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/demo')
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
    new_managerteam.save_mt()
    
    return redirect(url_for('index'))
      
  return render_template('page.html', form = mtform)


if __name__ == '__main__':
    app.run(debug=True)
    