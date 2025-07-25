from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/hello')
def hello():
    """
    A simple hello endpoint.
    ---
    responses:
      200:
        description: A successful response
        examples:
          application/json: {"message": "Hello, world!"}
    """
    return jsonify(message="Hello, world!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
