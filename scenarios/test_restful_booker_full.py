from pprint import pprint

from api.restful_booker import RestfulBooker
from assertpy import assert_that


def test_bookings_for_mark():
    rb_api = RestfulBooker()
    resp = rb_api.get_bookings('Suresh')
    pprint(resp.text)
    assert_that(resp.ok, 'HTTP Request OK').is_true()
    for booking in resp.json():
        assert_that(resp.ok, 'HTTP Request OK').is_true()
        resp2 = rb_api.describe_booking(booking['bookingid'])
        assert_that(resp2.json()["firstname"], 'Firstname').contains('Mark')



def test_addbooking():
    rb_api = RestfulBooker()
    resp = rb_api.add_random_booking()
    print(resp.json())
    assert_that(resp.ok, 'HTTP Request OK').is_true()
    # TODO construct a booking to create and assert created booking against it


def test_updatebooking():
    rb_api = RestfulBooker()
    auth_token = rb_api.get_authtoken()
    new_booking = rb_api.add_random_booking().json()['bookingid']
    resp = rb_api.update_booking(new_booking, auth_token)
    assert_that(resp.ok, 'HTTP Request OK').is_true()


def test_removebooking():
    rb_api = RestfulBooker()
    auth_token = rb_api.get_authtoken()
    print(auth_token)
    new_booking = rb_api.add_random_booking().json()['bookingid']
    resp = rb_api.remove_booking(new_booking, auth_token)
    pprint(resp.request.headers)
    pprint(resp.request.url)
    assert_that(resp.ok, 'HTTP Request OK').is_true()