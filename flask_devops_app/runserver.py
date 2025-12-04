"""
This script runs the FlaskWebProject1 application using a development server.
"""

from os import environ
from dotenv import load_dotenv
from FlaskWebProject1 import app

# Load environment variables from .env file
load_dotenv()

if __name__ == '__main__':
      app.run(host="0.0.0.0", port=8000)
