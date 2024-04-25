from pages.abtesting_page import ABTestingPage
from pages.home_page import HomePage


def test_disabling_abtest_works():
    aut = HomePage()
    aut.go_to_homepage()
    aut = aut.go_to_example('abtesting')
    title_before = aut.get_heading()
    assert title_before in ['A/B Test Variation 1', 'A/B Test Control']
    aut.disable_abtesting()
    aut.refresh_browser()
    title_after = aut.get_heading()
    assert title_after in ['No A/B Test']

