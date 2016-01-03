from flask import Flask,  jsonify


app = Flask(__name__)


# Default hello world route
@app.route('/')
def favicon():
    return jsonify({'message' : 'Hello pythonistic world'})


if __name__ == '__main__':
	app.run(threaded=True)