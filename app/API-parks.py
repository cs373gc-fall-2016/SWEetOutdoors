from bs4 import BeautifulSoup
import requests
import threading
from models import db, Park

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
statestran = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
        }
national_parks = ['Acadia National Park', 'Arches National Park', 'Badlands National Park', 'Big Bend National Park', 'Biscayne National Park', 
                  'Black Canyon of the Gunnison National Park', 'Bryce Canyon National Park', 'Canyonlands National Park', 'Capitol Reef National Park', 'Carlsbad Caverns National Park', 
                  'Channel Islands National Park', 'Congaree National Park', 'Crater Lake National Park', 'Cuyahoga Valley National Park', 'Death Valley National Park', 'Denali National Park', 
                  'Dry Tortugas National Park', 'Everglades National Park', 'Gates of the Arctic National Park', 'Glacier National Park', 'Glacier Bay National Park', 'Grand Canyon National Park', 
                  'Grand Teton National Park', 'Great Basin National Park', 'Great Sand Dunes National Park', 'Great Smoky Mountains National Park', 'Guadalupe Mountains National Park', 'Haleakala National Park', 
                  'Hawaii Volcanoes National Park', 'Hot Springs National Park', 'Isle Royale National Park', 'Joshua Tree National Park', 'Katmai National Park', 'Kenai Fjords National Park', 
                  'Kings Canyon National Park', 'Kobuk Valley National Park', 'Lake Clark National Park', 'Lassen Volcanic National Park', 'Mammoth Cave National Park', 'Mesa Verde National Park', 
                  'Mount Rainier National Park', 'North Cascades National Park', 'Olympic National Park', 'Petrified Forest National Park', 'Pinnacles National Park', 'Redwood National Park', 
                  'Rocky Mountain National Park', 'Saguaro National Park', 'Sequoia National Park', 'Shenandoah National Park', 'Theodore Roosevelt National Park', 'Virgin Islands National Park', 
                  'Voyageurs National Park', 'Wind Cave National Park', 'Wrangell St. Elias National Park', 'Yellowstone National Park', 'Yosemite National Park', 'Zion National Park']

az= ['a','b','c','d','e','f','g','h','i','j','k','l',
    'm','n','o','p','q','r','s','t','u','v','w','x','y','z']

base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="
end_url = "&key=AIzaSyAtY7qDs17_pSmKFlkEY1v3ieq1jKpy9og"

base_url2 = "https://maps.googleapis.com/maps/api/place/details/json?placeid="
end_url2 = "&key=AIzaSyAtY7qDs17_pSmKFlkEY1v3ieq1jKpy9og"

photo_url = "https://maps.googleapis.com/maps/api/place/photo?photoreference="
photo_end = "&key=AIzaSyAtY7qDs17_pSmKFlkEY1v3ieq1jKpy9og"

default_photo_url = "https://lh5.googleusercontent.com/xE0_qnkkeTcyG-02cl6MSxbojpcxUwKED2Hd5Aiu34aUL9UIrhC6bFCIPN1ov54dC9N1G1ahwzlV6A=w984-h755-rw"

def national_scrape():
    for string in national_parks:
        park_name = string
        string = string.replace(" ", "+")
        string = string.replace("-", "+")
        firsturl = base_url + string + end_url
        firstjson = requests.get(firsturl).json()
        if firstjson["status"] == "OK":
            print(len(firstjson["results"]))
            state_dict = firstjson["results"][0]
            #get place id and use place details api
            if len(state_dict) != 0:
                placeid = state_dict["place_id"]
                secondurl = base_url2 + placeid + end_url2
                secondjson = requests.get(secondurl).json()

                if secondjson["status"] != "OK":
                    print("well shit")
                    assert(False)


                result = secondjson["result"]
                state = ""
                for add in result["address_components"]:
                    if add["types"] == ["postal_code"]:
                        zipcode = add["short_name"]
                    if add["short_name"] in states:
                        state = add["long_name"]
                #zipcodeset.add(zipcode)
                print(state)
                address = result["formatted_address"]
                try:
                    phone = result["formatted_phone_number"]
                except KeyError:
                    phone = "(555) 555-5555"

                if "rating" in result:
                    rate = result["rating"]
                else:
                    raters = 0
                    rate = 0.0
                    try:
                        length = len(result["reviews"])
                    except KeyError:
                        length = 0
                    if length != 0:
                        for user in result["reviews"]:
                            rate += int(user["rating"])
                            raters += 1
                        rate = rate/raters
                    else:
                        rate = 3.0

                photo_link = photo_url
                zipregion = zipcode[0:3]

                try:
                    website = result["website"]
                except KeyError:
                    website = "http://www.sweetoutdoors.me/"

                try:
                    photo_stuff = result["photos"][0]
                    photo_link = photo_link + photo_stuff["photo_reference"]
                    photo_link = photo_link + "&maxheight=" + str(photo_stuff["height"])
                    photo_link = photo_link + "&maxwidth=" + str(photo_stuff["width"]) + photo_end  
                except KeyError:
                    photo_link = default_photo_url

                latitude = str(result["geometry"]["location"]["lat"])
                longitude = str(result["geometry"]["location"]["lng"])
                #convert to STRING LATLONG
                
                park_obj = Park(park_name, latitude, longitude, address, phone,
                                        rate, website, zipcode, photo_link, zipregion, state)
                db.session.add(park_obj)
            if state_dict != {}:
                print("done for %s" %park_name)
            state_dict = {}
        else:
            #NO RESULTS
            print(firstjson["status"])
    db.session.commit()
    db.session.close()

def state_scrape(begin, end):
    d = {}
    num = 0
    for letter in az:
        d[letter] = num
        num += 1

    state_dict  = {}

    #2372
    #4616
    #NOT ALL STATE PARKS ARE IN GOOGLE MAPS 

    for i in range(begin, end):
        state = states[i]
        url = "http://www.stateparks.com/" + state + ".html"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        flag = True
        for parkdiv in soup.find_all(id="parklink"):
            string = parkdiv.get_text()
            if flag:
                currentletter = d[string[0].lower()]
                flag = False
            if currentletter <= d[string[0].lower()]:
                currentletter = d[string[0].lower()]
                park_name = string
                string = string.replace(" ", "+")
                string = string.replace("-", "+")
                firsturl = base_url + string + end_url
                firstjson = requests.get(firsturl).json()
                if firstjson["status"] == "OK":
                    for dic in firstjson["results"]:
                        if state in dic["formatted_address"]:
                            #gets all the address w/ correct state
                            state_dict = dic
                            break
                    #get place id and use place details api
                    if len(state_dict) != 0:
                        placeid = state_dict["place_id"]
                        secondurl = base_url2 + placeid + end_url2
                        secondjson = requests.get(secondurl).json()

                        if secondjson["status"] != "OK":
                            print("well shit")
                            assert(False)


                        result = secondjson["result"]
                        for add in result["address_components"]:
                            if add["types"] == ["postal_code"]:
                                zipcode = add["short_name"]
                        
                        zipregion = zipcode[0:3]


                        address = result["formatted_address"]
                        try:
                            phone = result["formatted_phone_number"]
                        except KeyError:
                            phone = "(555) 555-5555"

                        if "rating" in result:
                            rate = result["rating"]
                        else:
                            raters = 0
                            rate = 0.0
                            try:
                                length = len(result["reviews"])
                            except KeyError:
                                
                                length = 0
                            if length != 0:
                                for user in result["reviews"]:
                                    rate += int(user["rating"])
                                    raters += 1
                                rate = rate/raters
                            else:
                                rate = 3.0

                        photo_link = photo_url

                        try:
                            website = result["website"]
                        except KeyError:
                            website = "http://www.sweetoutdoors.me/"

                        try:
                            photo_stuff = result["photos"][0]
                            photo_link = photo_link + photo_stuff["photo_reference"]
                            photo_link = photo_link + "&maxheight=" + str(photo_stuff["height"])
                            photo_link = photo_link + "&maxwidth=" + str(photo_stuff["width"]) + photo_end  
                        except KeyError:
                            photo_link = default_photo_url

                        latitude = str(result["geometry"]["location"]["lat"])
                        longitude = str(result["geometry"]["location"]["lng"])

                        park_obj = Park(park_name, latitude, longitude, address, phone,
                                        rate, website, zipcode, photo_link, zipregion, statestran[state])
                        db.session.add(park_obj)

                    if state_dict != {}:
                        print("done for %s" % park_name)
                    state_dict = {}
                else:
                    #NO RESULTS
                    print(firstjson["status"])
            else:
                break
    db.session.commit()
    db.session.close()

threads = []
indexthreads = [0, 10, 20, 31, 41]

for i in range(0, 5):
    start = i * 10
    end = start + 9
    thread = threading.Thread(target=state_scrape, args=(start, end))
    threads.append(thread)


national_scrape()

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()