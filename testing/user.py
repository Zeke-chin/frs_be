import unittest
from pathlib import Path

import requests
from faker import Faker

url = "http://localhost:8080"


def upload_img(img_path):
    with open(img_path, 'rb') as f:
        img = f.read()
    files = {'up_file': ("t.jpg", img)}
    r = requests.post(f'{url}/file', files=files)
    return r.json()['data']


def send_request(data):
    r = requests.post(f'{url}/create', json=data)
    print(r.json())
    return r.json()


class TestUser(unittest.TestCase):

    def test_create(self):
        user_img_path = Path("/Users/zeke/work/mediapipe/LFW/lfw/Edward_Said/Edward_Said_0001.jpg")
        user_name = user_img_path.parent.name
        user_email = f"{user_name}@example.com"
        user_head_img = upload_img(user_img_path)
        r = requests.post(f'{url}/user/',
                          json={
                              "name": user_name,
                              "head_img": user_head_img,
                              "email": user_email
                          })
        print(r.json()['data'])
        self.assertEquals(r.json()['code'], 200, 'status should be 200')

    def test_delete(self):
        user_id = 5
        r = requests.delete(f'{url}/user/{user_id}')
        print(r.json())
        self.assertEquals(r.json()['code'], 200, 'status should be 200')
