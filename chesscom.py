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

class ChessCom():
    """ The 4pc ChessCom api handler. """
    def __init__(self, token, url, version):
        self.version = version
        self.token = token
	self.header = []
        self.baseUrl = url
        self.session = requests.Session()
        self.set_user_agent("?")

    def is_final(exception):
        return isinstance(exception, HTTPError) and exception.response.status_code < 500

    @backoff.on_exception(backoff.constant,
        (RemoteDisconnected, ConnectionError, ProtocolError, HTTPError, ReadTimeout),
        max_time=60,
        interval=0.1,
        giveup=is_final)
    def api_get(self, path):
        url = urljoin(self.baseUrl, path)
        response = self.session.get(url, timeout=2)
        response.raise_for_status()
        return response.json()

    # Keep incase chesscom adds a post route.
    @backoff.on_exception(backoff.constant,
        (RemoteDisconnected, ConnectionError, ProtocolError, HTTPError, ReadTimeout),
        max_time=60,
	interval=0.1,
        giveup=is_final)
    def api_post(self, path, data=None):
        url = urljoin(self.baseUrl, path)
        response = self.session.post(url, data=data, timeout=2)
        response.raise_for_status()
        return response.json()

    def clear(self):
        url = urljoin(self.baseUrl, ENDPOINTS["clear"].format(self.token))
        return requests.get(url, headers=self.header, stream=True)

    def play(self, fromCoordinate, toCoordinate, promotionCode):
        url = urljoin(self.baseUrl, ENDPOINTS["arrow"].format(self.token, fromCoordinate + toCoordinate + promotionCode))
        return requests.get(url, headers=self.header, stream=True)

    def chat(self, text):
        url = urljoin(self.baseUrl, ENDPOINTS["chat"].format(self.token, text))
        return requests.get(url, headers=self.header, stream=True)

    def arrow(self, fromCoordinate, toCoordinate):
        url = urljoin(self.baseUrl, ENDPOINTS["arrow"].format(self.token, fromCoordinate + toCoordinate))
        return requests.get(url, headers=self.header, stream=True)

    def circle(self, coordinate):
        url = urljoin(self.baseUrl, ENDPOINTS["circle"].format(self.token, coordinate + coordinate))
        return requests.get(url, headers=self.header, stream=True)

    def get_game_stream(self):
        url = urljoin(self.baseUrl, ENDPOINTS["stream"].format(self.token))
        return requests.get(url, headers=self.header, stream=True)

    def resign(self):
        url = urljoin(self.baseUrl, ENDPOINTS["resign"].format(self.token))
        return requests.get(url, headers=self.header, stream=True)

    def set_user_agent(self, username):
        self.header.update({"User-Agent": "chesscom-bot/{} user:{}".format(self.version, username)})
        self.session.headers.update(self.header)
