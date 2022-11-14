
import psycopg2
from flask import Flask, render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://wpepkodmgckzze:02be78245346d6bc03fa4e5e667e3904529f762923b9ce6f3c5527cbf06c5858@ec2-34-230-153-41.compute-1.amazonaws.com:5432/d79mtf79npaf4h'


@app.route('/')
def hello():
  
  return render_template('page.html')


if __name__ == '__main__':
    app.run(debug=True)
    