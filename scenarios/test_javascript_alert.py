from pages.home_page import HomePage
from pages.javascript_alerts_page import JavaScriptAlertsPage


def test_simple_alert():
    # english
    aut = HomePage()
    aut.go_to_homepage()
    aut = aut.go_to_example("javascriptalerts")
    aut.invoke_simple_alert()
    message_in_alert = aut.get_message()
    aut.accept_message()
    assert message_in_alert == "I am a JS Alert"
    result_message = aut.get_result()
    assert result_message == "You successfully clicked an alert"


def test_simple_alert_tamil():
    # Tamil
    aut = HomePage()
    aut.go_to_homepage()
    aut = aut.go_to_example("javascriptalerts")
    aut.invoke_simple_alert()
    message_in_alert = aut.get_message()
    aut.accept_message()
    assert message_in_alert == "I am a JS Alert"
    result_message = aut.get_result()
    assert result_message == "You successfully clicked an alert"
