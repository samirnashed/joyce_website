from flask import Flask
from routes import setup_routes
import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../../templates'),static_folder=os.path.join(os.path.dirname(__file__), '../static'),)

setup_routes(app)

if __name__ == '__main__':
    app.run(debug=True)