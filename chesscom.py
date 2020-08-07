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
    "play": "/bot?token={}&play={}",
    "stream": "/bot?token={}&stream=1"
}

class ChessCom():
    def __init__(self, token, url, version):
        self.version = version
        self.token = token
        self.baseUrl = url
        self.session = requests.Session()
        self.set_user_agent("?")

    def is_final(exception):
	""" Determine if this request is final. """
        return isinstance(exception, HTTPError) and exception.response.status_code < 500

    @backoff.on_exception(backoff.constant,
        (RemoteDisconnected, ConnectionError, ProtocolError, HTTPError, ReadTimeout),
        max_time=60,
        interval=0.1,
        giveup=is_final)
    def api_get(self, path):
	""" Preform a get request. """
        url = urljoin(self.baseUrl, path)
        response = self.session.get(url, timeout=2)
        response.raise_for_status()
        return response.json()

    def clear(self):
	""" Clears all of the arrows on the board. """
        return self.api_get(ENDPOINTS["arrow"].format(self.token, "clear"))

    def play(self, move):
        """ Preforms a move on the board. """
        return self.api_get(ENDPOINTS["play"].format(self.token, move))

    def chat(self, text):
	""" Sends a message to the chat. """
        return self.api_get(ENDPOINTS["chat"].format(self.token, text))

    def arrow(self, arrow):
	""" Sends an arrow to the board. """
        return self.api_get(ENDPOINTS["arrow"].format(self.token, arrow))

    def circle(self, move):
	""" Sends a circle to the board. """
        return self.api_get(ENDPOINTS["circle"].format(self.token, move + move))

    def get_game_stream(self):
        """ Gets the games stream data. """
        url = urljoin(self.baseUrl, ENDPOINTS["stream"].format(self.token))
        return requests.get(url, headers = self.header, stream = True)

    def resign(self):
	""" Resigns the current game. """
        return self.api_get(ENDPOINTS["play"].format(self.token, "R"))

    def set_user_agent(self, username):
	""" Sets the user agent. """
        self.header.update({"User-Agent": "chesscom-bot/{} user:{}".format(self.version, username)})
        self.session.headers.update(self.header)
