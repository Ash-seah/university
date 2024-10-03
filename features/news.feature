Feature: News Management

  Scenario: Create a new news item
    Given I have a news payload with description "Breaking News" and notification_id 1
    When I send a POST request to "/news/"
    Then the response status code should be 200
    And the response should contain news with description "Breaking News"

  Scenario: Update an existing news item
    Given a news item exists with id 1 and description "Old News"
    When I send a PUT request to "/news/1/" with description "Updated News"
    Then the response status code should be 200
    And the response should contain news with description "Updated News"

  Scenario: Delete a news item
    Given a news item exists with id 1
    When I send a DELETE request to "/news/1/"
    Then the response status code should be 200
    And the response should contain a message "News deleted successfully"

  Scenario: Retrieve all news items
    Given news items exist
    When I send a GET request to "/news/"
    Then the response status code should be 200
    And the response should contain a list of news items
