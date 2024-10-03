Feature: Manage Courses
  Scenario: Update a course
    Given a course exists with ID 1
    And the updated course data is provided
    When I send a PUT request to "/courses/1"
    Then the course should be updated successfully
    And the response should contain the updated course details

  Scenario: Delete a course
    Given a course exists with ID 1
    When I send a DELETE request to "/courses/1"
    Then the course should be deleted successfully
    And the response should confirm the deletion
