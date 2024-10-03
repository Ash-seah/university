Feature: Classes Management

  Scenario: Create a new class
    Given I have a class payload with name "Math 101" and description "Basic Math Class"
    When I send a POST request to "/classes/"
    Then the response status code should be 200
    And the response should contain a class with name "Math 101"

  Scenario: Update an existing class
    Given a class exists with id 1 and name "Old Class"
    When I send a PUT request to "/classes/1/" with name "Updated Class"
    Then the response status code should be 200
    And the response should contain a class with name "Updated Class"

  Scenario: Delete a class
    Given a class exists with id 1
    When I send a DELETE request to "/classes/1/"
    Then the response status code should be 200
    And the response should contain a message "Class deleted successfully"

  Scenario: Retrieve all classes
    Given classes exist
    When I send a GET request to "/classes/"
    Then the response status code should be 200
    And the response should contain a list of classes
