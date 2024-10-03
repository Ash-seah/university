Feature: Manage Courses
  Scenario: Delete a course
    Given a course exists with ID 1
    When I send a DELETE request to "/courses/1"
    Then the course should be deleted successfully
    And the response should confirm the deletion

  Scenario: Create a new notification
    Given the notification data is provided
    When I send a POST request to "/notifications/"
    Then the notification should be created successfully
    And the response should contain the notification details

  Scenario: Get all notifications
    Given there are notifications in the database
    When I send a GET request to "/notifications/"
    Then I should receive a list of all notifications
