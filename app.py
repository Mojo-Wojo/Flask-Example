from flask import Flask, request, jsonify
from middleware import simple_middleware, validator
from server import create_server

app = Flask(__name__)

# Apply middleware
app.wsgi_app = simple_middleware(app.wsgi_app)

# Define a route to validate input
@app.route('/validate', methods=['POST'])
def validate_input():
    data = request.get_json()
    input_string = data.get('input_string', '')
    if validator(input_string):
        return jsonify({'message': 'Input contains numbers'}), 400
    return jsonify({'message': 'Input is valid'}), 200

if __name__ == '__main__':
    create_server(app)
