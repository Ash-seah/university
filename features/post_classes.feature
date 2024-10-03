Feature: Create Class

  Scenario: Successfully create a new class
    Given the user is on the class creation page
    When the user enters valid class details
      | name        | description       | subject   |
      | Math 101    | Basic Math course | Mathematics |
    And the user submits the class creation form
    Then the class should be created successfully
    And the response should contain the class details
      | name        | description       | subject   |
      | Math 101    | Basic Math course | Mathematics |

  Scenario: Fail to create a class with missing details
    Given the user is on the class creation page
    When the user enters incomplete class details
      | name        | description       | subject   |
      | Math 101    |                   | Mathematics |
    And the user submits the class creation form
    Then the user should receive an error message
    And the error message should indicate missing description
