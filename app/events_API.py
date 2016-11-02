import requests
from models import db, Event

# use ramboho virtual enviornment which is in top level directory
# current page = offset
# per_page = rows per page


per_page = 1200
current_page=0

url = "http://api.amp.active.com/v2/search?per_page=1&current_page=0&start_date=2016-08-01..2017-12-31&category=trail%20heads&api_key=kww96xbnrt8a3dj6ndfkdyzx"
response = requests.get(url)

data = response.json()

numResponses = 0
numResponses = int(data["total_results"])
print(numResponses)
numPages = numResponses // per_page + 1
print(numPages)
# categories = set()
# topics = set()

# print(results)
count = 0
while current_page < numPages:
	url = "http://api.amp.active.com/v2/search?per_page="+str(per_page)+"&current_page="+str(current_page)+"&start_date=2016-08-01..2017-12-31&category=trail%20heads&api_key=kww96xbnrt8a3dj6ndfkdyzx"
	response = requests.get(url)
	# print(url)

	data = response.json()

	# numResponses = data["total_results"]
	# numPages = numResponses // per_page + 1
	# leftover = numResponses % per_page

	results = data["results"]		#dictionary
	for event in results:
		# print(event)
		count += 1

		invalidEvent = False
		state = ""
		zipcode = ""
		try:
			longitude = event["place"]["geoPoint"]["lon"]
			latitude = event["place"]["geoPoint"]["lat"]
			# location_json = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng="+latitude+","+longitude+"&key=AIzaSyD6F3rB8GtFapIpn9YG-GmqW_aGisnY5s8").json()
			# for comp in location_json["results"][0]["address_components"]:
			# 	if(comp["types"][0] == "administrative_area_level_1"):
			# 		state = comp["long_name"]
			# 	elif(comp["types"][0] == "postal_code"):
			# 		zipcode = comp["long_name"]
		except KeyError as err:
			invalidEvent = True
			# print("KeyError: {0}".format(err))
			# print("nothing works")

		if not invalidEvent:
			# Topics
			first = True
			topics = "" 
			for topic in event["assetTopics"]:
				if first:
					topics += topic["topic"]["topicName"]
					first = False
				else:
					topics += ", "+topic["topic"]["topicName"]
			# print(topics)

			endDate = event["activityEndDate"]
			startDate = event["activityStartDate"]
			
			picUrl = event["logoUrlAdr"]
			eventUrl = event["urlAdr"]
			
			orgName = event["organization"]["organizationName"]
			zipcode = event["organization"]["addressPostalCd"]
			contactPhoneNum = event["organization"]["primaryContactPhone"]
			orgUrl = event["homePageUrlAdr"]
			city = event["place"]["cityName"]

			#add to database <---------
			eventInstance = Event(latitude, longitude, topics, startDate, endDate, picUrl, eventUrl, orgName, 
                 contactPhoneNum, orgUrl, zipcode, city)
			#print(eventInstance)
		#print("***********************did it print?")
			db.session.add(eventInstance)
			# print("begin commit")
			db.session.commit()
			# print("  end commit")

		
	current_page += 1

db.session.close()

# print(topics)
# print(categories)