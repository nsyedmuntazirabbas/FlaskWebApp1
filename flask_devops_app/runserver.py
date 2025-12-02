"""
This script runs the FlaskWebProject1 application using a development server.
"""

from os import environ
from dotenv import load_dotenv
from FlaskWebProject1 import app

# Load environment variables from .env file
load_dotenv()

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(environ.get('SERVER_PORT', '8000'))
    except ValueError:
        PORT = 5555
    app.run(host=HOST, port=PORT)
