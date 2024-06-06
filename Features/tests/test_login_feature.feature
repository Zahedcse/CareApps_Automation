# Created by zahed at 21/4/24
Feature: Login test suite
  All the login test cases will be included here
  Scenario: Admin will try to login using valid creds
    Given User will open the login page
    When User input username and password
    And User will hit submit button
    Then user will login and see a message

    