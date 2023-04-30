Feature: viewing the list of orders made by user

Scenario: user wants to view the list of orders they made
    Given user is on the homepage
    When user logs in and clicks on the orders button 
    Then user can see the list of orders they have made