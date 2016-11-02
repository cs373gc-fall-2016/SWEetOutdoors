import requests
from models import db, Campground

states = {
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

base_url = "https://ridb.recreation.gov/api/v1/facilities/?apikey=871320D83EEA46098DAA776A31288331&activity=9"
facilities_json = requests.get(base_url).json()
num_facilities = facilities_json["METADATA"]["RESULTS"]["TOTAL_COUNT"]
# print(num_facilities)
facility_offset = 0
while facility_offset < num_facilities:
    facilities_json = requests.get(base_url + "&offfset=" + str(facility_offset)).json()
    for facility in facilities_json["RECDATA"]:
        name = facility["FacilityName"]
        description = facility["FacilityDescription"]
        cost = facility["FacilityUseFeeDescription"]
        latitude = facility["FacilityLatitude"]
        longitude = facility["FacilityLongitude"]
        accessibilty = facility["FacilityAdaAccess"]
        reservation_url = facility["FacilityReservationURL"]
        email = facility["FacilityEmail"]
        facility_id = facility["FacilityID"]

        # location_json = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(latitude) + "," + str(longitude) + "&key=AIzaSyD6F3rB8GtFapIpn9YG-GmqW_aGisnY5s8").json()
        # print("https://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(latitude) + "," + str(longitude) + "&key=AIzaSyD6F3rB8GtFapIpn9YG-GmqW_aGisnY5s8")
        # print(location_json["results"])
        # print("----------------------------")
        # print(location_json["results"][0])
        # print("----------------------------")
        # print(location_json["results"][0]["address_components"])
        # print("----------------------------")

        # for comp in location_json["results"][0]["address_components"]:
        #     if(comp["types"][0] == "administrative_area_level_1"):
        #         state = comp["long_name"]
        #     elif(comp["types"][0] == "postal_code"):
        #         zipcode = comp["long_name"]

        # print("http://dev.virtualearth.net/REST/v1/Locations/" + str(latitude) + "," + str(longitude) + "?o=xml&key=AnVzFw_MvQU64BLJ6gJ4CBx0JSJUCnWom08V9AeBVcInE4caAJnazgcfPdN54J-0")
        location_json = requests.get("http://dev.virtualearth.net/REST/v1/Locations/" + str(latitude) + "," + str(longitude) + "?key=AnVzFw_MvQU64BLJ6gJ4CBx0JSJUCnWom08V9AeBVcInE4caAJnazgcfPdN54J-0").json()
        
        state = states[location_json["resourceSets"][0]["resources"][0]["address"]["adminDistrict"]]
        zipcode = location_json["resourceSets"][0]["resources"][0]["address"]["postalCode"]

        campgroundInstance = Campground(name, description, cost, latitude, longitude, accessibilty,
                 reservation_url, email, zipcode, state)  
        db.session.add(campgroundInstance)   

    print(facility_offset)
    facility_offset += 50
db.session.commit()
db.session.close()
