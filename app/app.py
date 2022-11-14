import os
import psycopg2
from flask import Flask, render_template

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')




app = Flask(__name__)


@app.route('/route_name')
def method_name():
    pass

@app.route('/')
def hello():
  
  return render_template('page.html')


if __name__ == '__main__':
    app.run(debug=True)
    