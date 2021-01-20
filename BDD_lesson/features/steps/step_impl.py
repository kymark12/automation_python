from api_lesson.post_api_example import *
from behave import given, when, then


@given('the book details which needs to be added to Library')
def stepImpl(context):
    context.urls = [getConfig()['API']['endpoint'] + ApiResources.add_book,
                    getConfig()['API']['endpoint'] + ApiResources.delete_book]
    context.headers = {"Content-Type": "application/json"}
    context.payload = buildPayLoadFromDB(query)


@when(u'we execute the AddBook PostAPI method')
def step_impl(context):
    context.addbook_response = requests.post(context.urls[0], json=context.payload,
                                             headers=context.headers)


@then(u'Book is successfully added')
def step_impl(context):
    print(context.addbook_response.json())

    res_json = context.addbook_response.json()
    print(type(res_json))

    context.bk_id = response_json['ID']
    print(context.bk_id)
    print(res_json['msg'])
    #  assert res_json['msg'] == "successfully added"


@given('Book details {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    context.urls = [getConfig()['API']['endpoint'] + ApiResources.add_book,
                    getConfig()['API']['endpoint'] + ApiResources.delete_book]
    context.headers = {"Content-Type": "application/json"}
    context.payload = addBookPayload(isbn, aisle)
