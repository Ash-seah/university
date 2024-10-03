Feature: User Registration

  Scenario: Successful user registration
    Given the user data is valid
    When I send a POST request to "/register/" with the user data
    Then the response status code should be 200
    And the response message should be "User registered successfully."

  Scenario: User registration with existing username
    Given the user data has an existing username
    When I send a POST request to "/register/" with the user data
    Then the response status code should be 400
    And the response message should be "User with this username or email already exists."

  Scenario: User registration with existing email
    Given the user data has an existing email
    When I send a POST request to "/register/" with the user data
    Then the response status code should be 400
    And the response message should be "User with this username or email already exists."

  Scenario: User registration with missing fields
    Given the user data is missing required fields
    When I send a POST request to "/register/" with the incomplete user data
    Then the response status code should be 422
    And the response should indicate the missing fields
