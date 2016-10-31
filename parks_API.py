from bs4 import BeautifulSoup
import requests 

#base_url = "https://en.wikipedia.org/wiki/Lists_of_state_parks_by_U.S._state"
url = "https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
table = soup.find('table')
data = []
rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('th')
    name = [ele.text.strip() for ele in cols]
    for ele in cols:
        data.append(ele.text.strip() + " National Park") 


print (data[7:])

"""['Acadia National Park', 'American Samoa National Park', 'Arches National Park', 'Badlands National Park', 'Big Bend National Park', 'Biscayne National Park', 'Black Canyon of the Gunnison National Park', 'Bryce Canyon National Park', 'Canyonlands National Park', 'Capitol Reef National Park', 'Carlsbad Caverns National Park', 'Channel Islands National Park', 'Congaree National Park', 'Crater Lake National Park', 'Cuyahoga Valley National Park', 'Death Valley National Park', 'Denali National Park', 'Dry Tortugas National Park', 'Everglades National Park', 'Gates of the Arctic National Park', 'Glacier National Park', 'Glacier Bay National Park', 'Grand Canyon National Park', 'Grand Teton National Park', 'Great Basin National Park', 'Great Sand Dunes National Park', 'Great Smoky Mountains National Park', 'Guadalupe Mountains National Park', 'Haleakalā National Park', 'Hawaii Volcanoes National Park', 'Hot Springs National Park', 'Isle Royale National Park', 'Joshua Tree National Park', 'Katmai National Park', 'Kenai Fjords National Park', 'Kings Canyon National Park', 'Kobuk Valley National Park', 'Lake Clark National Park', 'Lassen Volcanic National Park', 'Mammoth Cave National Park', 'Mesa Verde National Park', 'Mount Rainier National Park', 'North Cascades National Park', 'Olympic National Park', 'Petrified Forest National Park', 'Pinnacles National Park', 'Redwood National Park', 'Rocky Mountain National Park', 'Saguaro National Park', 'Sequoia National Park', 'Shenandoah National Park', 'Theodore Roosevelt National Park', 'Virgin Islands National Park', 'Voyageurs National Park', 'Wind Cave National Park', 'Wrangell–St. Elias National Park', 'Yellowstone National Park', 'Yosemite National Park', 'Zion National Park']"""
