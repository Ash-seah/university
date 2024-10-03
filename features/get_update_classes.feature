Feature: Get Classes

  Scenario: Successfully retrieve all classes
    Given the user is on the classes page
    When the user requests the list of classes
    Then the user should receive a list of classes
    And the list should contain class details
      | name        | description       | subject   |
      | Math 101    | Basic Math course | Mathematics |
      | Physics 101 | Basic Physics     | Physics     |

  Scenario: Successfully update an existing class
    Given the user is on the class update page
    When the user enters valid updated class details
      | name        | description       | subject   |
      | Math 102    | Advanced Math     | Mathematics |
    And the user submits the class update form
    Then the class should be updated successfully
    And the response should contain the updated class details
      | name        | description       | subject   |
      | Math 102    | Advanced Math     | Mathematics |

  Scenario: Fail to update a non-existent class
    Given the user is on the class update page
    When the user enters valid updated class details for a non-existent class
      | name        | description       | subject   |
      | Math 102    | Advanced Math     | Mathematics |
    And the user submits the class update form
    Then the user should receive an error message
    And the error message should be "Class not found"
