import requests
from bs4 import BeautifulSoup


data = requests.get("https://www.imdb.com/find?s=ep&q=Thriller&ref_=nv_sr_sm")
soup = BeautifulSoup(data.content, "html.parser")
# print(soup.prettify())
movies_table = soup.find('table', {"class": 'findList'})
# print(movies_table.prettify())
rows = movies_table.findAll('tr')
li = []
for row in rows:
    row_data = row.findAll('td')
    sub_url = row_data[1].a['href']
    sub_data = requests.get("https://www.imdb.com/"+sub_url)
    sub_soup = BeautifulSoup(sub_data.content, 'html.parser')
    if sub_soup.find('div', {'class': 'see-more inline canwrap'}):
        genre = sub_soup.find('div', {'class': 'see-more inline canwrap'})
        if genre.a.text == "Documentary":
            # print(row_data[1].a.text)
            # print(genre.a.text)
            li.append(row_data[1].a.text)
print(li)
