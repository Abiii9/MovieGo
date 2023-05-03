Feature: logging out user

Scenario: user wants to logout of the application
    Given user is on the homepage for logout and already logged in
    When user clicks on the logout button 
    Then user is able to log out of the application