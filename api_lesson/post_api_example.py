import requests
from api_lesson.payload_methods import *
from api_lesson.utilities.resources import *
from api_lesson.utilities.configuration import *


urls = [getConfig()['API']['endpoint'] + ApiResources.add_book,
        getConfig()['API']['endpoint'] + ApiResources.delete_book]

book_payload = {
    "name": "Learn API Automation with Python",
    "isbn": "OXCV31",
    "aisle": "20122",
    "author": "Aya"
}

query = 'select * from Books'

addbook_response = requests.post(urls[0], json=buildPayLoadFromDB(query),
                                 headers={"Content-Type": "application/json"})

print(addbook_response.json())

response_json = addbook_response.json()
print(type(response_json))

book_id = response_json['ID']

# Delete book

response_deletebook = requests.post(urls[1], json={"ID": book_id},
                                    headers={"Content-Type": "application/json"})
assert response_deletebook.status_code == 200
response_message_delete = response_deletebook.json()
response_message = response_message_delete["msg"]

print(response_message)
assert response_message == "book is successfully deleted"
