import requests
from requests import Request
from views.meta import AUTHORIZATION, HOST


def get_token(login: str, password: str):
    try:
        token = requests.post(f'{HOST.URL}/token',
                              data={'grant_type': '', 'username': login, 'password': password,
                                    'scope': '', 'client_id': '', 'client_secret': ''})

        if token.status_code != 401:
            AUTHORIZATION.TOKEN = token.json()['access_token']
            return AUTHORIZATION.TOKEN
        else:
            return None
    except:
        pass


def send(req: Request):
    token = AUTHORIZATION.TOKEN
    req.headers['Authorization'] = f"Bearer {token}"
    s = requests.Session()
    resp = s.send(req.prepare())
    return resp


def get_my_profile():
    req = requests.Request('GET', f'{HOST.URL}/users/me')
    resp = send(req)
    return resp.json()
