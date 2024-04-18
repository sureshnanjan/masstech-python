@python
Feature: Python Data Structures
  @datastructures
  Scenario: Python Odd Even Items from lists
    Given I have the following lists
    |collection|
    |3,6,9,12,15,18,21|
    |4,8,12,16,20,24,28|
    When I ask python to use the strategy
    |list|type|
    |1|odd|
    |2|even|
    Then python should give me the result
      """
      6,12,18,4,12,20,28
      """

    @selenium
    Scenario: Heroku app title is working OK
        Given I visit heroku app
        When I check the title
        Then it should match "Welcome to the-internet"
