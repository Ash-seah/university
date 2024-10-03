from behave import given, when, then
import requests
from datetime import datetime

BASE_URL = "http://localhost:8000"

@given('I have a notification payload with slug "{slug}"')
def step_given_notification_payload(context, slug):
    context.notification_payload = {"slug": slug}

@when('I send a POST request to "/notifications/"')
def step_when_post_notification(context):
    response = requests.post(f"{BASE_URL}/notifications/", json=context.notification_payload)
    context.response = response

@then('the response status code should be {status_code}')
def step_then_status_code(context, status_code):
    print("context response:" + context.response.content)
    print("context response:" + context.response.status_code)
    assert context.response.status_code == status_code

@then('the response should contain a notification with slug "{slug}"')
def step_then_notification_slug(context, slug):
    response_data = context.response.json()
    assert response_data["slug"] == slug

@given('a notification exists with id {notification_id:d} and slug "{slug}"')
def step_given_existing_notification(context, notification_id, slug):
    # This step assumes the notification already exists in the database.
    # You might need to set up the database state before running the tests.
    pass

@when('I send a PUT request to "/notifications/{notification_id}/" with slug "{slug}"')
def step_when_put_notification(context, notification_id, slug):
    response = requests.put(f"{BASE_URL}/notifications/{notification_id}/", json={"slug": slug})
    context.response = response

@given('a notification exists with id {notification_id:d}')
def step_given_notification_exists(context, notification_id):
    # This step assumes the notification already exists in the database.
    pass

@when('I send a DELETE request to "/notifications/{notification_id}/"')
def step_when_delete_notification(context, notification_id):
    response = requests.delete(f"{BASE_URL}/notifications/{notification_id}/")
    context.response = response

@then('the response should contain a message "{message}"')
def step_then_response_message(context, message):
    response_data = context.response.json()
    assert response_data["message"] == message

@given('notifications exist')
def step_given_notifications_exist(context):
    # This step assumes notifications already exist in the database.
    pass

@when('I send a GET request to "/notifications/"')
def step_when_get_notifications(context):
    response = requests.get(f"{BASE_URL}/notifications/")
    context.response = response

@then('the response should contain a list of notifications')
def step_then_list_of_notifications(context):
    response_data = context.response.json()
    assert isinstance(response_data, list)

@given('I have a news payload with description "{description}" and notification_id {notification_id:d}')
def step_given_news_payload(context, description, notification_id):
    context.news_payload = {"description": description, "notification_id": notification_id}

@when('I send a POST request to "/news/"')
def step_when_post_news(context):
    response = requests.post(f"{BASE_URL}/news/", json=context.news_payload)
    context.response = response

@then('the response should contain news with description "{description}"')
def step_then_news_description(context, description):
    response_data = context.response.json()
    assert response_data["description"] == description

@given('a news item exists with id {news_id:d} and description "{description}"')
def step_given_existing_news(context, news_id, description):
    # This step assumes the news item already exists in the database.
    pass

@when('I send a PUT request to "/news/{news_id}/" with description "{description}"')
def step_when_put_news(context, news_id, description):
    response = requests.put(f"{BASE_URL}/news/{news_id}/", json={"description": description})
    context.response = response

@given('a news item exists with id {news_id:d}')
def step_given_news_exists(context, news_id):
    # This step assumes the news item already exists in the database.
    pass

@when('I send a DELETE request to "/news/{news_id}/"')
def step_when_delete_news(context, news_id):
    response = requests.delete(f"{BASE_URL}/news/{news_id}/")
    context.response = response

@given('news items exist')
def step_given_news_items_exist(context):
    # This step assumes news items already exist in the database.
    pass

@when('I send a GET request to "/news/"')
def step_when_get_news(context):
    response = requests.get(f"{BASE_URL}/news/")
    context.response = response

@then('the response should contain a list of news items')
def step_then_list_of_news(context):
    response_data = context.response.json()
    assert isinstance(response_data, list)

@given('I have a discount payload with quantity {quantity:d}, start_time "{start_time}", end_time "{end_time}", notification_id {notification_id:d}, and class_id {class_id:d}')
def step_given_discount_payload(context, quantity, start_time, end_time, notification_id, class_id):
    context.discount_payload = {
        "quantity": quantity,
        "start_time": datetime.fromisoformat(start_time),
        "end_time": datetime.fromisoformat(end_time),
        "notification_id": notification_id,
        "class_id": class_id
    }

@when('I send a POST request to "/discounts/"')
def step_when_post_discount(context):
    response = requests.post(f"{BASE_URL}/discounts/", json=context.discount_payload)
    context.response = response

@then('the response should contain a discount with quantity {quantity:d}')
def step_then_discount_quantity(context, quantity):
    response_data = context.response.json()
    assert response_data["quantity"] == quantity

@given('a discount exists with id {discount_id:d} and quantity {quantity:d}')
def step_given_existing_discount(context, discount_id, quantity):
    # This step assumes the discount already exists in the database.
    pass

@when('I send a PUT request to "/discounts/{discount_id}/" with quantity {quantity:d}')
def step_when_put_discount(context, discount_id, quantity):
    response = requests.put(f"{BASE_URL}/discounts/{discount_id}/", json={"quantity": quantity})
    context.response = response

@given('a discount exists with id {discount_id:d}')
def step_given_discount_exists(context, discount_id):
    # This step assumes the discount already exists in the database.
    pass

@when('I send a DELETE request to "/discounts/{discount_id}/"')
def step_when_delete_discount(context, discount_id):
    response = requests.delete(f"{BASE_URL}/discounts/{discount_id}/")
    context.response = response

@given('discounts exist')
def step_given_discounts_exist(context):
    # This step assumes discounts already exist in the database.
    pass

@when('I send a GET request to "/discounts/"')
def step_when_get_discounts(context):
    response = requests.get(f"{BASE_URL}/discounts/")
    context.response = response

@then('the response should contain a list of discounts')
def step_then_list_of_discounts(context):
    response_data = context.response.json()
    assert isinstance(response_data, list)

@given('I have a class payload with name "{name}" and description "{description}"')
def step_given_class_payload(context, name, description):
    context.class_payload = {"name": name, "description": description}

@when('I send a POST request to "/classes/"')
def step_when_post_class(context):
    response = requests.post(f"{BASE_URL}/classes/", json=context.class_payload)
    context.response = response

@then('the response should contain a class with name "{name}"')
def step_then_class_name(context, name):
    response_data = context.response.json()
    assert response_data["name"] == name

@given('a class exists with id {class_id:d} and name "{name}"')
def step_given_existing_class(context, class_id, name):
    # This step assumes the class already exists in the database.
    pass

@when('I send a PUT request to "/classes/{class_id}/" with name "{name}"')
def step_when_put_class(context, class_id, name):
    response = requests.put(f"{BASE_URL}/classes/{class_id}/", json={"name": name})
    context.response = response

@given('a class exists with id {class_id:d}')
def step_given_class_exists(context, class_id):
    # This step assumes the class already exists in the database.
    pass

@when('I send a DELETE request to "/classes/{class_id}/"')
def step_when_delete_class(context, class_id):
    response = requests.delete(f"{BASE_URL}/classes/{class_id}/")
    context.response = response

@given('classes exist')
def step_given_classes_exist(context):
    # This step assumes classes already exist in the database.
    pass

@when('I send a GET request to "/classes/"')
def step_when_get_classes(context):
    response = requests.get(f"{BASE_URL}/classes/")
    context.response = response

@then('the response should contain a list of classes')
def step_then_list_of_classes(context):
    response_data = context.response.json()
    assert isinstance(response_data, list)

@given('I have a course payload with subject "{subject}", description "{description}", number_of_sessions {number_of_sessions:d}, and discount_id {discount_id:d}')
def step_given_course_payload(context, subject, description, number_of_sessions, discount_id):
    context.course_payload = {
        "subject": subject,
        "description": description,
        "number_of_sessions": number_of_sessions,
        "discount_id": discount_id
    }

@when('I send a POST request to "/courses/"')
def step_when_post_course(context):
    response = requests.post(f"{BASE_URL}/courses/", json=context.course_payload)
    context.response = response

@then('the response should contain a course with subject "{subject}"')
def step_then_course_subject(context, subject):
    response_data = context.response.json()
    assert response_data["subject"] == subject

@given('a course exists with id {course_id:d} and subject "{subject}"')
def step_given_existing_course(context, course_id, subject):
    # This step assumes the course already exists in the database.
    pass

@when('I send a PUT request to "/courses/{course_id}/" with subject "{subject}"')
def step_when_put_course(context, course_id, subject):
    response = requests.put(f"{BASE_URL}/courses/{course_id}/", json={"subject": subject})
    context.response = response

@given('a course exists with id {course_id:d}')
def step_given_course_exists(context, course_id):
    # This step assumes the course already exists in the database.
    pass

@when('I send a DELETE request to "/courses/{course_id}/"')
def step_when_delete_course(context, course_id):
    response = requests.delete(f"{BASE_URL}/courses/{course_id}/")
    context.response = response

@given('courses exist')
def step_given_courses_exist(context):
    # This step assumes courses already exist in the database.
    pass

@when('I send a GET request to "/courses/"')
def step_when_get_courses(context):
    response = requests.get(f"{BASE_URL}/courses/")
    context.response = response

@then('the response should contain a list of courses')
def step_then_list_of_courses(context):
    response_data = context.response.json()
    assert isinstance(response_data, list)
