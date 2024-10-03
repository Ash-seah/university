from behave import given, when, then
import requests

BASE_URL = "http://localhost:8000"

@given('I have the user registration endpoint')
def step_given_(context):
    context.url = f"{BASE_URL}/register/"

@when('I register a new user with username "{username}", email "{email}", and password "{password}"')
def step_impl(context, username, email, password):
    context.response = requests.post(context.url, json={
        "username": username,
        "email": email,
        "password": password
    })

@then('I should receive a message "{message}"')
def step_impl(context, message):
    assert context.response.json()["message"] == message

@given('I have the user login endpoint')
def step_impl(context):
    context.url = f"{BASE_URL}/login/"

@when('I login with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.response = requests.post(context.url, json={
        "username": username,
        "password": password
    })

@given('I have the class creation endpoint')
def step_impl(context):
    context.url = f"{BASE_URL}/classes/"

@when('I create a class with name "{name}" and description "{description}"')
def step_impl(context, name, description):
    context.response = requests.post(context.url, json={
        "name": name,
        "description": description
    })

@then('the class should be created with name "{name}" and description "{description}"')
def step_impl(context, name, description):
    response_data = context.response.json()
    assert response_data["name"] == name
    assert response_data["description"] == description
