import requests

response = requests.get('http://216.10.245.166/Library/GetBook.php',
                        params={"AuthorName": 'Mark Ivan'})
# print(response.text)
# print(type(response.text))
# response_string = response.text
# dict_response = json.loads(response_string)
# print(type(dict_response))  # it's a list because of the response's container as [ ]

# simple method in parsing requests
json_response = response.json()
print(type(json_response))
print(json_response[0]['isbn'])
assert response.status_code == 200
print(response.headers)
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'

# Retrieve the book details with ISBN RGHCC
expected_book = {
        "book_name": "Learn API Automation with RestAssured",
        "isbn": "RGHCC",
        "aisle": "12239"
}
for actual_book in json_response:
    if actual_book['isbn'] == 'RGHCC':
        assert actual_book == expected_book


