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

  Scenario: Create a Riazi class
    Given I have the Riazi creation endpoint
    When I create a Riazi class with name "Riazi 101", description "Basic Riazi class", and class_id 1
    Then the Riazi class should be created with name "Riazi 101" and description "Basic Riazi class"

  Scenario: Create a Tajrobi class
    Given I have the Tajrobi creation endpoint
    When I create a Tajrobi class with name "Tajrobi 101", description "Basic Tajrobi class", and class_id 1
    Then the Tajrobi class should be created with name "Tajrobi 101" and description "Basic Tajrobi class"

  Scenario: Create an Ensani class
    Given I have the Ensani creation endpoint
    When I create an Ensani class with name "Ensani 101", description "Basic Ensani class", and class_id 1
    Then the Ensani class should be created with name "Ensani 101" and description "Basic Ensani class"

  Scenario: Create a teacher
    Given I have the teacher creation endpoint
    When I create a teacher with name "John Doe", subject "Math", and class_id 1
    Then the teacher should be created with name "John Doe" and subject "Math"
