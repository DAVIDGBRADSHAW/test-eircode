
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    address = request.form['address']
  return render_template('index.html', result=None)

if __name__ == '__main__':
  app.run(debug=True)