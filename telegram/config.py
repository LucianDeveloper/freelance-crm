from os import environ
import logging

logging.basicConfig(level=logging.INFO)

TOKEN = environ.get('TOKEN_TG', '5016209053:AAEyy1GhYVUc-zePBUD4SP9HhZkYJQbNftc')
URL_BACKEND = environ.get('URL_BACKEND', 'http://127.0.0.1:8000/api')

if URL_BACKEND.startswith('http:'):
    WS_BACKEND = URL_BACKEND.replace('http://', 'ws://')
else:
    WS_BACKEND = URL_BACKEND.replace('https://', 'wss://')

FRONTEND_APP = environ.get('ALLOW_CORS', 'http://127.0.0.1:3000')

logger = logging.getLogger(__name__)
