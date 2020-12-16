import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from api_lesson.utilities.configuration import *


se = requests.session()
se.auth = auth = ('kymark12', getPassword())

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
url = 'https://api.github.com/user'
github_response = se.get(url, verify=False)
print(github_response.status_code)

url2 = "https://api.github.com/user/repos"
response = se.get(url2)
print(response.status_code)
