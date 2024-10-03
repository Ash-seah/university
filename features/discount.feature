Feature: Discounts Management

  Scenario: Create a new discount
    Given I have a discount payload with quantity 10, start_time "2023-01-01T00:00:00", end_time "2023-01-31T23:59:59", notification_id 1, and class_id 1
    When I send a POST request to "/discounts/"
    Then the response status code should be 200
    And the response should contain a discount with quantity 10

  Scenario: Update an existing discount
    Given a discount exists with id 1 and quantity 5
    When I send a PUT request to "/discounts/1/" with quantity 15
    Then the response status code should be 200
    And the response should contain a discount with quantity 15

  Scenario: Delete a discount
    Given a discount exists with id 1
    When I send a DELETE request to "/discounts/1/"
    Then the response status code should be 200
    And the response should contain a message "Discount deleted successfully"

  Scenario: Retrieve all discounts
    Given discounts exist
    When I send a GET request to "/discounts/"
    Then the response status code should be 200
    And the response should contain a list of discounts
