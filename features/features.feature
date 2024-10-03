Feature: User Management

  Scenario: User registration
    Given I have the user registration endpoint
    When I register a new user with username "testuser", email "test@example.com", and password "password"
    Then I should receive a message "User registered successfully."

  Scenario: User login
    Given I have the user login endpoint
    When I login with username "testuser" and password "password"
    Then I should receive a message "Login successful"

  Scenario: Create a class
    Given I have the class creation endpoint
    When I create a class with name "Math" and description "Mathematics class"
    Then the class should be created with name "Math" and description "Mathematics class"