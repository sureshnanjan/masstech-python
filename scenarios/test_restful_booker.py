from api.restful_booker import RestfulBooker


def test_health_check_ok():
    rbtester = RestfulBooker()
    response = rbtester.do_health_check()
    assert response.status_code == 201


def test_auth_returns_json_for_correct_creds():
    rbtester = RestfulBooker()
    response = rbtester.get_auth_token('admin', 'password123')
    assert len(response.json()['token']) == 15
    #response.



def test_auth_fails_for_wrong_creds():
    rbtester = RestfulBooker()
    response = rbtester.get_auth_token('wrong', 'password123')
    #response = rbtester.postman_code();
    assert len(response.json()['token']) == 15
