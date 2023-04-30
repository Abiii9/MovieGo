Feature: sign up new users

Scenario: new user wants to sign in to the application
    Given user is on the home page and clicks signup
    When user enters details and submits
    Then user is able to sign up to be a customer of the application