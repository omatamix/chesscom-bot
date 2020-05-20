import requests
from urllib.parse import urljoin
from requests.exceptions import ConnectionError, HTTPError, ReadTimeout
from urllib3.exceptions import ProtocolError

try:
    from http.client import RemoteDisconnected
    # New in version 3.5: Previously, BadStatusLine('') was raised.
except ImportError:
    from http.client import BadStatusLine as RemoteDisconnected

import backoff

ENDPOINTS = {
    "arrow": "/bot?token={}&arrow={}",
    "chat": "/bot?token={}&chat={}",
    "circle": "/bot?token={}&arrow={}",
    "clear": "/bot?token={}&arrow=clear",
    "play": "/bot?token={}&arrow{}",
    "resign": "/bot?token={}&play=R",
    "stream": "/bot?token={}&stream=1"
}

