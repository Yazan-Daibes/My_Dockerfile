from app import app
from flask import jsonify, request

@app.route('/')
def hello():
	return 'Hello, I am Yazan Daibes!'


@app.route('/how are you')
def how_are_you():
	return 'I am good, how about you?'

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

