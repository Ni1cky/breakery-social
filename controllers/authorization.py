import requests
from requests import Request
from views.meta import AUTHORIZATION

def get_token(login: str, password: str):
    token = requests.post('http://127.0.0.1:8000/token',
                          data={'grant_type': '', 'username': login, 'password': password,
                                'scope': '', 'client_id': '', 'client_secret': ''})
    AUTHORIZATION.TOKEN = token.json()['access_token']
    return AUTHORIZATION.TOKEN


def send(req: Request):
    token = AUTHORIZATION.TOKEN
    req.headers['Authorization'] = f"Bearer {token}"
    s = requests.Session()
    resp = s.send(req.prepare())
    return resp

def get_my_profile():
    req = requests.Request('GET', 'http://127.0.0.1:8000/users/me')
    resp = send(req)
    return resp.json()