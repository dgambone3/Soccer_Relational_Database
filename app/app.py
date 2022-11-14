from flask import Flask, render_template
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


app = Flask(__name__)


@app.route('/route_name')
def method_name():
    pass

@app.route('/')
def hello():
  
  return render_template('page.html')


if __name__ == '__main__':
    app.run(debug=True)
    