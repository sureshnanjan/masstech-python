import json

import requests
from requests import HTTPError, Request, Response, get
from utilities.api_data import GenerateDataRB


class RestfulBooker:
    def __init__(self):
        self.url = 'https://restful-booker.herokuapp.com'
        self.token = None

    def get_auth_token(self, uname, password):
        payload = json.dumps({
            "username": f"{uname}",
            "password": f"{password}"
        })
        response = requests.post(f"{self.url}/auth",
                                 data=payload,
                                 headers={"Content-Type":"application/json"})
        response.raise_for_status()
        return response

    def _url(self, path):
        return f"{self.url}{path}"

    def do_health_check(self):
        response = get(f"{self.url}/ping")
        #get
        response.raise_for_status()
        raw_data = response.content
        text_data = response.text
        status_code = response.status_code
        return response

    def get_bookings(self,firstname="", lastname="", checkin="", checkout=""):
        payload = {}
        if firstname:
            payload['firstname'] = firstname
        if lastname:
            payload['lastname'] = lastname
        if checkin:
            payload['checkin'] = checkin
        if checkout:
            payload['checkout'] = checkout

        if payload:
            return requests.get(self._url('/booking/'), params=payload)
        else:
            return requests.get(self._url('/booking/'))

    def describe_booking(self, booking_id):
        return requests.get(self._url('/booking/{:d}/'.format(booking_id)))

    def add_random_booking(self):
        return self.add_booking(GenerateDataRB.generate_booking())


    def add_booking(self, booking):
        return requests.post(self._url('/booking/'), json=booking)

    def remove_booking(self, booking_id, auth_token):
        return requests.delete(self._url(f"/booking/:{booking_id}/"), cookies={
            "token": auth_token
        })

    def update_booking(self, booking_id, auth_token, firstname='Jim', lastname='Brown', totalprice=111, depositpaid=True,
                       checkin='2018-01-01', checkout='2019-01-01', additionalneeds='Breakfast'):
        return requests.put(self._url(f"/booking/:{booking_id}/"), json={
            "firstname": firstname,
            "lastname": lastname,
            "totalprice": totalprice,
            "depositpaid": depositpaid,
            "bookingdates": {
                "checkin": checkin,
                "checkout": checkin
            },
            "additionalneeds": additionalneeds
        }, cookies={
            "token": auth_token
        })

    def get_authtoken(self, username='admin', password='password123'):
        url = self._url('/auth')
        return requests.post(url, json={
            "username": username,
            "password": password
        }).json()['token']

    def postman_code(self):
        import requests
        import json
        url = "https://restful-booker.herokuapp.com/auth"
        payload = json.dumps({
            "username": "admin",
            "password": "password123"
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response



