Feature: Heroku Web app Demo features
  Scenario: Home Page heading is matching
    Given I Have Heroku app opened
    When I check the main heading
    Then it should match "Welcome to the-internet"