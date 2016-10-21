from models import db

# creates the database
db.create_all()

# state instances
#name, highestPoint, population, description, total_area
db.add(State("Texas", 8751, 27469114, "Texas is the second largest state in the United States by both area and population. Geographically located in the south central part of the country, Texas shares borders with the other US states of Louisiana to the east, Arkansas to the northeast, Oklahoma to the north, New Mexico to the west, and the Mexican states of Chihuahua, Coahuila, Nuevo León, and Tamaulipas to the southwest, while the Gulf of Mexico is to the southeast.", 268581))
db.add(State("California", 14505, 39144818, "California is the most populous state in the United States. It is also the third most extensive by area. Los Angeles, in Southern California, is the state's most populous city and the country's second largest after New York City. California also includes the nation's most populous county, Los Angeles County, and the largest county by area, San Bernardino County. Geographically located in the western part of the United States, California is bordered by the other United States states of Oregon to the north, Nevada to the east, and Arizona to the southeast. California shares an international border with the Mexican state of Baja California to the south and the Pacific Ocean is on the state's western coastline. The state capital is Sacramento, which is located in the northern part of the state. A majority of California's cities are located in either the San Francisco Bay Area or the Sacramento metropolitan area in Northern California; or the Los Angeles area, the Riverside-San Bernardino-Inland Empire, or the San Diego metropolitan area in Southern California.", 163696)
db.add(State("Florida", 345, 20271272, "Florida (Spanish for "land of flowers") is a state located in the southeastern region of the United States. The state is bordered to the west by the Gulf of Mexico, to the north by Alabama and Georgia, to the east by the Atlantic Ocean, and to the south by the Straits of Florida and Cuba. Florida is the 22nd most extensive, the 3rd most populous,[8] and the 8th most densely populated of the United States. Jacksonville is the most populous city in Florida, and the largest city by area in the contiguous United States. The Miami metropolitan area is the eighth-largest metropolitan area in the United States. Tallahassee is the state capital.", 65755))

name, latitude, longitude, electricity, water, sewer, pets, park_id_fk, state_id_fk):
db.add(Campground("Alamosa KOA", 37.4744444, -105.7986111, TRUE, TRUE, FALSE, TRUE, 1, 2))
db.add()
