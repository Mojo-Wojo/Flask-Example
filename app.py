from flask import Flask, request, jsonify
from middleware import simple_middleware, validator
from server import create_server
import sqlite3

app = Flask(__name__)

# Apply middleware
app.wsgi_app = simple_middleware(app.wsgi_app)

# Initialize the database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Define a route to validate input and query the database
@app.route('/validate', methods=['POST'])
def validate_input():
    data = request.get_json()
    input_string = data.get('input_string', '')

    # Validate the input string
    if validator(input_string):
        return jsonify({'message': 'Input contains numbers'}), 400

    # Query the database for matching results
    conn = get_db_connection()
    cursor = conn.execute('SELECT * FROM your_table WHERE column_name = ?', (input_string,))
    results = cursor.fetchall()
    conn.close()

    if results:
        return jsonify({'message': 'Matches found', 'results': [dict(row) for row in results]}), 200
    else:
        return jsonify({'message': 'No matches found'}), 404

if __name__ == '__main__':
    create_server(app)
