import requests
from json import loads

from src.person import Person
from src.magiclist import MagicList

NO_TOKEN_MSG = "Couldn't get access token."
NO_NORMALIZE_MSG = "Couldn't get the normalize data."


def test_api():
    """Test normalize API"""
    r = requests.post('http://localhost:8888/auth',
                      json={'username': 'Admin', 'password': 'Admin'},
                      headers={'Content-Type': 'application/json'})
    if r.ok:
        access_token = loads(r.content)['access_token']
    else:
        print(NO_TOKEN_MSG)

    r = requests.post('http://localhost:8888/normalize',
                      json={'data': [{'metadata': 'not interesting', 'name': 'device', 'strVal': 'iPhone'},
                                     {'boolVal': 'false', 'lastSeen': 'not interesting', 'name': 'isHuman'}]},
                      headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {access_token}'})
    if r.ok:
        print(loads(r.content))
    else:
        print(NO_NORMALIZE_MSG)


def test_magic_list():
    """Test MagicList"""
    k = MagicList(cls_type=Person)
    k[0] = 2
    k[1] = 3
    k[2].age = 5
    print(k)


def main():
    test_api()
    test_magic_list()


if __name__ == '__main__':
    main()
