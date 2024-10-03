from behave import given, when, then
import requests

BASE_URL = "http://localhost:8000"

@given('I have the user registration endpoint')
def step_impl(context):
    assert requests.get(f"{BASE_URL}/register/").status_code == 200
    context.url = f"{BASE_URL}/register/"

@when('I register a new user with username "{username}", email "{email}", and password "{password}"')
def step_impl(context, username, email, password):
    context.response = requests.post(context.url, json={
        "username": username,
        "email": email,
        "password": password
    })
    assert context.response.status_code == 200

@then('I should receive a message "{message}"')
def step_impl(context, message):
    assert context.response.json()["message"] == message

@given('I have the user login endpoint')
def step_impl(context):
    assert requests.get(f"{BASE_URL}/login/").status_code == 200
    context.url = f"{BASE_URL}/login/"

@when('I login with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.response = requests.post(context.url, json={
        "username": username,
        "password": password
    })
    assert context.response.status_code == 200

@given('I have the class creation endpoint')
def step_impl(context):
    assert requests.get(f"{BASE_URL}/classes/").status_code == 200
    context.url = f"{BASE_URL}/classes/"

@when('I create a class with name "{name}" and description "{description}"')
def step_impl(context, name, description):
    context.response = requests.post(context.url, json={
        "name": name,
        "description": description
    })
    assert context.response.status_code == 200

@then('the class should be created with name "{name}" and description "{description}"')
def step_impl(context, name, description):
    response_data = context.response.json()
    assert response_data["name"] == name
    assert response_data["description"] == description

@given('I have the Riazi creation endpoint')
def step_impl(context):
    assert requests.get(f"{BASE_URL}/register/").status_code == 200
    context.url = f"{BASE_URL}/riazi/"

@when('I create a Riazi class with name "{name}", description "{description}", and class_id {class_id}')
def step_impl(context, name, description, class_id):
    context.response = requests.post(context.url, json={
        "name": name,
        "description": description,
        "class_id": class_id
    })
    assert context.response.status_code == 200

@then('the Riazi class should be created with name "{name}" and description "{description}"')
def step_impl(context, name, description):
    response_data = context.response.json()
    assert response_data["name"] == name
    assert response_data["description"] == description

@given('I have the Tajrobi creation endpoint')
def step_impl(context):
    context.url = f"{BASE_URL}/tajrobi/"

@when('I create a Tajrobi class with name "{name}", description "{description}", and class_id {class_id}')
def step_impl(context, name, description, class_id):
    context.response = requests.post(context.url, json={
        "name": name,
        "description": description,
        "class_id": class_id
    })
    assert context.response.status_code == 200

@then('the Tajrobi class should be created with name "{name}" and description "{description}"')
def step_impl(context, name, description):
    response_data = context.response.json()
    assert response_data["name"] == name
    assert response_data["description"] == description

@given('I have the Ensani creation endpoint')
def step_impl(context):
    context.url = f"{BASE_URL}/ensani/"

@when('I create an Ensani class with name "{name}", description "{description}", and class_id {class_id}')
def step_impl(context, name, description, class_id):
    context.response = requests.post(context.url, json={
        "name": name,
        "description": description,
        "class_id": class_id
    })
    assert context.response.status_code == 200

@then('the Ensani class should be created with name "{name}" and description "{description}"')
def step_impl(context, name, description):
    response_data = context.response.json()
    assert response_data["name"] == name
    assert response_data["description"] == description

@given('I have the teacher creation endpoint')
def step_impl(context):
    context.url = f"{BASE_URL}/teachers/"

@when('I create a teacher with name "{name}", subject "{subject}", and class_id {class_id}')
def step_impl(context, name, subject, class_id):
    context.response = requests.post(context.url, json={
        "name": name,
        "subject": subject,
        "class_id": class_id
    })
    assert context.response.status_code == 200

@then('the teacher should be created with name "{name}" and subject "{subject}"')
def step_impl(context, name, subject):
    response_data = context.response.json()
    assert response_data["name"] == name
    assert response_data["subject"] == subject
