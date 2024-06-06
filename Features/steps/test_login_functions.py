from behave import *


@given("User will open the login page")
def step_impl(context):
    context.app.login_page.open_url()


@when("User input username and password")
def step_impl(context):
    context.app.login_page.input_email()
    context.app.login_page.input_password()


@step("User will hit submit button")
def step_impl(context):
    context.app.login_page.submit()


@then("user will login and see a message")
def step_impl(context):
    context.app.login_page.assert_login_message()
