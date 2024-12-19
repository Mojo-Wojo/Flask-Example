from flask import Flask
from middleware import simple_middleware, validator
from server import create_server

app = Flask(__name__)

# Apply middleware
app.wsgi_app = simple_middleware(app.wsgi_app)

# Define a simple route
@app.route('/')
def home():
    return 'Hello, Flask!'

if __name__ == '__main__':
    create_server(app)
