from bs4 import BeautifulSoup
import requests 

url = "http://en.wikipedia.org/wiki/List_of_Alabama_state_parks"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
table = soup.find('table')
data = []
rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)

print (data)
