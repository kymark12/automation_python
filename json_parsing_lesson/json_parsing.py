import json


courses = '{"name": "Mark Ivan Berbenzana", "languages": ["Java", "Python"]}'

# Loads method parse json string and it returns dictionary

dict_courses = json.loads(courses)
print(type(dict_courses))
print(dict_courses)
print(dict_courses['name'])

# get me the first language taught by trainer

# list_of_languages = dict_courses['languages']  # store the list parameters on the dictionary into a variable
# print(type(list_of_languages))  # verify the data type
# print(list_of_languages[1])  # choose the language

print(dict_courses['languages'][0])

# ******** Parse content present in Json file
with open('D:\\Selenium Python\\course.json') as f:
    data = json.load(f)
    # print(data)
    print(type(data))
    print(data['courses'][1]['title'])  # To navigate to a specific value

# Price of RPA
    print(type(data['courses']))
    for course in data['courses']:
        print(course)
        if course['title'] == "RPA":
            print(course['price'])
            assert course['price'] == 45

# Comparing two Json Schemas using Python Dictionaries
with open('D:\\Selenium Python\\course2.json') as fi:
    data2 = json.load(fi)
    print(data == data2)  # in python, this how easy it is to compare 2 JSONs unlike other languages
