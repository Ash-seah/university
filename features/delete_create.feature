Feature: Delete Class

  Scenario: Successfully delete an existing class
    Given the user is on the class deletion page
    When the user deletes a class with ID 1
    Then the class should be deleted successfully
    And the response should contain a success message

  Scenario: Fail to delete a non-existent class
    Given the user is on the class deletion page
    When the user deletes a class with a non-existent ID
    Then the user should receive an error message
    And the error message should be "Class not found"

  Scenario: Successfully create a new course
    Given the user is on the course creation page
    When the user enters valid course details
      | subject       | description       | number_of_sessions | discount_id |
      | Mathematics   | Advanced Math     | 10                 | 1           |
    And the user submits the course creation form
    Then the course should be created successfully
    And the response should contain the course details
      | subject       | description       | number_of_sessions | discount_id |
      | Mathematics   | Advanced Math     | 10                 | 1           |

  Scenario: Fail to create a course with missing details
    Given the user is on the course creation page
    When the user enters incomplete course details
      | subject       | description       | number_of_sessions | discount_id |
      | Mathematics   |                   | 10                 | 1           |
    And the user submits the course creation form
    Then the user should receive an error message
    And the error message should indicate missing description
