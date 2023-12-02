from flask import Flask, render_template
import pytest

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/hello/<name>')
def hello_name(name):
	return 'Hello %s!' % name

@app.route('/<value>')
def hello_value(value):
	print("Value Printed")
	print(value)
	return 'Value printed on Command Line'

@app.route('/mult/<number>')
def hello_number(number):
	print(number)
	mult = 5 * int(number)
	print(mult)
	return str(mult)

if __name__ == '__main__':
 app.run(port='8080', host='0.0.0.0')
