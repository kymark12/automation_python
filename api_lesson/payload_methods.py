from api_lesson.utilities.configuration import *


def addBookPayload(isbn, aisle):
    body = {
        "name": "Learn API Automation with Python",
        "isbn": isbn,
        "aisle": aisle,
        "author": "Aya"
    }
    return body


def buildPayLoadFromDB(query):
    addBody = {}
    tp = getQuery(query)
    addBody['name'] = tp[0]
    addBody['isbn'] = tp[1] + tp[2]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]
    return addBody
