import requests
from api_lesson.payload_methods import *
from api_lesson.utilities.resources import *
from api_lesson.utilities.configuration import *
from behave import given, when, then


@given('the book details which needs to be added to Library')
def stepImpl(context):
    context.urls = [getConfig()['API']['endpoint'] + ApiResources.add_book,
                    getConfig()['API']['endpoint'] + ApiResources.delete_book]
    context.headers = {"Content-Type": "application/json"}
    context.payload = addBookPayload("testng32", '34323')


@when(u'we execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.urls[0], json=context.payload, headers=context.headers)


@then(u'Book is successfully added')
def step_impl(context):
    print(context.response.json())
    res_json = context.response.json()

    context.bk_id = res_json['ID']
    print(res_json['Msg'])
    assert res_json['Msg'] == 'successfully added'


@given('Book details {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    context.urls = [getConfig()['API']['endpoint'] + ApiResources.add_book,
                    getConfig()['API']['endpoint'] + ApiResources.delete_book]
    context.headers = {"Content-Type": "application/json"}
    context.payload = addBookPayload(isbn, aisle)


@given('I have github auth credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = ('kymark12', getPassword())


@when('I hit getRepo API of github')
def step_impl(context):
    context.response = context.se.get(ApiResources.github_repo)


@then('status code response should be {expected_status:d}')
def step_impl(context, expected_status):
    print(context.response.status_code)
    assert context.response.status_code == expected_status
