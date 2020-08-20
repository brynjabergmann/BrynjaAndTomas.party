"""
This script runs the DublinProject application using a development server.
"""

from os import environ, urandom
from DublinProject import app

if __name__ == '__main__':
    app.secret_key = urandom(12)

    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
