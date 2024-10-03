from behave import given, when, then
import requests

BASE_URL = "http://localhost:8000"

@given('the user data is valid')
def step_impl(context):
    context.user_data = {
        "username": "newuser",
        "email": "newuser@example.com",
        "password": "securepassword"
    }

@given('the user data has an existing username')
def step_impl(context):
    context.user_data = {
        "username": "existinguser",
        "email": "newemail@example.com",
        "password": "securepassword"
    }

@given('the user data has an existing email')
def step_impl(context):
    context.user_data = {
        "username": "newuser",
        "email": "existingemail@example.com",
        "password": "securepassword"
    }

@given('the user data is missing required fields')
def step_impl(context):
    context.user_data = {
        "username": "newuser"
        # Missing email and password
    }

@when('I send a POST request to "/register/" with the user data')
def step_impl(context):
    context.response = requests.post(f"{BASE_URL}/register/", json=context.user_data)

@then('the response status code should be {status_code:d}')
def step_impl(context, status_code):
    assert context.response.status_code == status_code

@then('the response message should be "{message}"')
def step_impl(context, message):
    assert context.response.json().get("message") == message

@then('the response should indicate the missing fields')
def step_impl(context):
    response_json = context.response.json()
    assert "detail" in response_json
    assert response_json["detail"][0]["msg"] == "field required"

## login

from behave import given, when, then
import requests

@given('the user is on the login page')
def step_impl(context):
    context.base_url = 'http://localhost:8000/login/'

@when('the user enters valid credentials')
def step_impl(context):
    context.response = requests.post(context.base_url, json={"username": "testuser", "password": "testpass"})

@when('the user enters invalid credentials')
def step_impl(context):
    context.response = requests.post(context.base_url, json={"username": "testuser", "password": "wrongpass"})

@when('the user submits the login form')
def step_impl(context):
    pass  # This step is handled in the previous steps

@then('the user should receive an access token')
def step_impl(context):
    assert context.response.status_code == 200
    assert "access_token" in context.response.json()

@then('the token type should be "bearer"')
def step_impl(context):
    assert context.response.json()["token_type"] == "bearer"

@then('the user should receive an error message')
def step_impl(context):
    assert context.response.status_code == 401
    assert context.response.json()["detail"] == "Invalid credentials"

## classes

# features/steps/class_steps.py
from behave import given, when, then
import requests

@given('the user is on the class creation page')
def step_impl(context):
    context.base_url = 'http://localhost:8000/classes/'

@when('the user enters valid class details')
def step_impl(context):
    context.response = requests.post(context.base_url, json={
        "name": "Math 101",
        "description": "Basic Math course",
        "subject": "Mathematics"
    })

@when('the user enters incomplete class details')
def step_impl(context):
    context.response = requests.post(context.base_url, json={
        "name": "Math 101",
        "description": "",
        "subject": "Mathematics"
    })

@when('the user submits the class creation form')
def step_impl(context):
    pass  # This step is handled in the previous steps

@then('the class should be created successfully')
def step_impl(context):
    assert context.response.status_code == 200
    response_json = context.response.json()
    assert response_json["name"] == "Math 101"
    assert response_json["description"] == "Basic Math course"
    assert response_json["subject"] == "Mathematics"

@then('the response should contain the class details')
def step_impl(context):
    response_json = context.response.json()
    assert response_json["name"] == "Math 101"
    assert response_json["description"] == "Basic Math course"
    assert response_json["subject"] == "Mathematics"


@then('the error message should indicate missing description')
def step_impl(context):
    error_detail = context.response.json()["detail"]
    assert any("description" in error["loc"] for error in error_detail)



## get_update classes

# features/steps/class_steps.py
from behave import given, when, then
import requests

@given('the user is on the classes page')
def step_impl(context):
    context.base_url = 'http://localhost:8000/classes/'

@when('the user requests the list of classes')
def step_impl(context):
    context.response = requests.get(context.base_url)

@then('the user should receive a list of classes')
def step_impl(context):
    assert context.response.status_code == 200
    assert isinstance(context.response.json(), list)

@then('the list should contain class details')
def step_impl(context):
    response_json = context.response.json()
    assert any(class_["name"] == "Math 101" for class_ in response_json)
    assert any(class_["description"] == "Basic Math course" for class_ in response_json)
    assert any(class_["subject"] == "Mathematics" for class_ in response_json)

@given('the user is on the class update page')
def step_impl(context):
    context.base_url = 'http://localhost:8000/classes/1'  # Assuming class ID 1 for the example

@when('the user enters valid updated class details')
def step_impl(context):
    context.response = requests.put(context.base_url, json={
        "name": "Math 102",
        "description": "Advanced Math",
        "subject": "Mathematics"
    })

@when('the user enters valid updated class details for a non-existent class')
def step_impl(context):
    context.base_url = 'http://localhost:8000/classes/9999'  # Assuming non-existent class ID
    context.response = requests.put(context.base_url, json={
        "name": "Math 102",
        "description": "Advanced Math",
        "subject": "Mathematics"
    })

@then('the class should be updated successfully')
def step_impl(context):
    assert context.response.status_code == 200
    response_json = context.response.json()
    assert response_json["name"] == "Math 102"
    assert response_json["description"] == "Advanced Math"
    assert response_json["subject"] == "Mathematics"

@then('the response should contain the updated class details')
def step_impl(context):
    response_json = context.response.json()
    assert response_json["name"] == "Math 102"
    assert response_json["description"] == "Advanced Math"
    assert response_json["subject"] == "Mathematics"


## delete create


@given('the user is on the class deletion page')
def step_impl(context):
    context.base_url = 'http://localhost:8000/classes/'

@when('the user deletes a class with ID {class_id}')
def step_impl(context, class_id):
    context.response = requests.delete(f"{context.base_url}{class_id}")

@then('the class should be deleted successfully')
def step_impl(context):
    assert context.response.status_code == 200
    assert context.response.json()["message"] == "Class deleted successfully."


@given('the user is on the course creation page')
def step_impl(context):
    context.base_url = 'http://localhost:8000/courses/'

@when('the user enters valid course details')
def step_impl(context):
    context.response = requests.post(context.base_url, json={
        "subject": "Mathematics",
        "description": "Advanced Math",
        "number_of_sessions": 10,
        "discount_id": 1
    })

@when('the user enters incomplete course details')
def step_impl(context):
    context.response = requests.post(context.base_url, json={
        "subject": "Mathematics",
        "description": "",
        "number_of_sessions": 10,
        "discount_id": 1
    })

@then('the course should be created successfully')
def step_impl(context):
    assert context.response.status_code == 200
    response_json = context.response.json()
    assert response_json["subject"] == "Mathematics"
    assert response_json["description"] == "Advanced Math"
    assert response_json["number_of_sessions"] == 10
    assert response_json

## manage courses

@given('there are courses in the database')
def step_given_courses_in_database(context):
    # This step would ideally set up the database with some courses
    # For simplicity, we assume the database already has courses
    pass

@when('I send a GET request to "/courses/"')
def step_when_get_courses(context):
    response = requests.get(f"{BASE_URL}/courses/")
    context.response = response

@then('I should receive a list of all courses')
def step_then_receive_list_of_courses(context):
    assert context.response.status_code == 200
    assert isinstance(context.response.json(), list)

@given('the updated course data is provided')
def step_given_updated_course_data(context):
    context.updated_course_data = {
        "subject": "Physics",
        "description": "Advanced Physics",
        "number_of_sessions": 12,
        "discount_id": 2
    }

@when('I send a PUT request to "/courses/1"')
def step_when_update_course(context):
    response = requests.put(f"{BASE_URL}/courses/{context.course_id}", json=context.updated_course_data)
    context.response = response

@then('the course should be updated successfully')
def step_then_course_updated(context):
    assert context.response.status_code == 200

@then('the response should contain the updated course details')
def step_then_response_contains_updated_course_details(context):
    response_data = context.response.json()
    assert response_data["subject"] == context.updated_course_data["subject"]
    assert response_data["description"] == context.updated_course_data["description"]
    assert response_data["number_of_sessions"] == context.updated_course_data["number_of_sessions"]
    assert response_data["discount_id"] == context.updated_course_data["discount_id"]


@given('the notification data is provided')
def step_given_notification_data(context):
    context.notification_data = {
        "slug": "new-notification"
    }

@when('I send a POST request to "/notifications/"')
def step_when_create_notification(context):
    response = requests.post(f"{BASE_URL}/notifications/", json=context.notification_data)
    context.response = response

@then('the notification should be created successfully')
def step_then_notification_created(context):
    assert context.response.status_code == 200
    context.notification_id = context.response.json()["id"]

@then('the response should contain the notification details')
def step_then_response_contains_notification_details(context):
    response_data = context.response.json()
    assert response_data["slug"] == context.notification_data["slug"]

@given('there are notifications in the database')
def step_given_notifications_in_database(context):
    # This step would ideally set up the database with some notifications
    # For simplicity, we assume the database already has notifications
    pass

@when('I send a GET request to "/notifications/"')
def step_when_get_notifications(context):
    response = requests.get(f"{BASE_URL}/notifications/")
    context.response = response

@then('I should receive a list of all notifications')
def step_then_receive_list_of_notifications(context):
    assert context.response.status_code == 200
    assert isinstance(context.response.json(), list)

@given('a course exists with ID 1')
def step_given_course_exists(context):
    context.course_data = {
        "subject": "Math",
        "description": "Advanced Mathematics",
        "number_of_sessions": 10,
        "discount_id": 1
    }
    response = requests.post(f"{BASE_URL}/courses/", json=context.course_data)
    context.course_id = response.json()["id"]

@when('I send a DELETE request to "/courses/1"')
def step_when_delete_course(context):
    response = requests.delete(f"{BASE_URL}/courses/{context.course_id}")
    context.response = response

@then('the course should be deleted successfully')
def step_then_course_deleted(context):
    assert context.response.status_code == 200

@then('the response should confirm the deletion')
def step_then_response_confirms_deletion(context):
    response_data = context.response.json()
    assert response_data["message"] == "Course deleted successfully."
