Feature: Notifications Management

  Scenario: Create a new notification
    Given I have a notification payload with slug "new-notification"
    When I send a POST request to "/notifications/"
    Then the response status code should be 200
    And the response should contain a notification with slug "new-notification"

  Scenario: Update an existing notification
    Given a notification exists with id 1 and slug "old-notification"
    When I send a PUT request to "/notifications/1/" with slug "updated-notification"
    Then the response status code should be 200
    And the response should contain a notification with slug "updated-notification"

  Scenario: Delete a notification
    Given a notification exists with id 1
    When I send a DELETE request to "/notifications/1/"
    Then the response status code should be 200
    And the response should contain a message "Notification deleted successfully"

  Scenario: Retrieve all notifications
    Given notifications exist
    When I send a GET request to "/notifications/"
    Then the response status code should be 200
    And the response should contain a list of notifications
