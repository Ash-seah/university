Feature: User Login

  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters valid credentials
      | username | password |
      | testuser | testpass |
    And the user submits the login form
    Then the user should receive an access token
    And the token type should be "bearer"

  Scenario: Unsuccessful login with invalid credentials
    Given the user is on the login page
    When the user enters invalid credentials
      | username | password |
      | testuser | wrongpass |
    And the user submits the login form
    Then the user should receive an error message
    And the error message should be "Invalid credentials"
