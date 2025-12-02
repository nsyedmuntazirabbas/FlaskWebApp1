"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app
import psycopg2
import redis
from FlaskWebProject1 import config

# Initialize Redis client
redis_client = redis.StrictRedis(host=config.REDIS_HOST, port=config.REDIS_PORT, decode_responses=True)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/db-test')
def db_test():
    """Tests PostgreSQL database connection."""
    try:
        conn = psycopg2.connect(
            host=config.POSTGRES_HOST,
            database=config.POSTGRES_DB,
            user=config.POSTGRES_USER,
            password=config.POSTGRES_PASSWORD
        )
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        result = cur.fetchone()
        cur.close()
        conn.close()
        return f"Postgres Connected — Server Time: {result[0]}"
    except Exception as e:
        return f"Postgres Error: {str(e)}"


@app.route('/cache-test')
def cache_test():
    """Tests Redis cache connection."""
    try:
        count = redis_client.incr("visits")
        return f"Redis Connected - Visit Count: {count}"
    except Exception as e:
        return f"Redis Error: {str(e)}"


