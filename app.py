from eircode.address import Address
from flask import Flask, render_template, request

app = Flask(__name__)

def search_address(address, reverse=True):
  address = Address(address, proxy=False, reverse=reverse)
  return address.serialize()

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    address = request.form['address']
    result = search_address(address)
    print(result)
    return render_template('index.html', result=result)
  return render_template('index.html', result=None)

if __name__ == '__main__':
  app.run(debug=True)