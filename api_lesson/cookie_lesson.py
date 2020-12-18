import requests


# Initial cookie request
cookie = {'visit-month': 'February'}
response_cookie = requests.get('http://rahulshettyacademy.com', allow_redirects=False,
                               cookies=cookie, timeout=1)
# print(response_cookie.history)
print(response_cookie.status_code)

# Session manager
se = requests.session()
se.cookies.update({'visit-month': 'February'})

# Adding Session manager to a new request so that last request can be attached
response = se.get('http://httpbin.org/cookies', cookies={'visit-year': '2022'})
print(response.text)

# Attachments lesson
url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
files = {'file': open('D:\\Pictures\\test.png', 'rb')}
r = requests.post(url, files=files)
print(r.status_code)
print(r.text)
