import wptools 
import wikipedia
import re 
from models import db, State

#Louisiana, Kansas , Maine, Minnesota, 
states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida',
    'Georgia (U.S. state)','Hawaii','Idaho','Illinois',
    'Indiana','Iowa','Kentucky','Maryland','Massachusetts','Michigan',
    'Mississippi','Missouri','Nebraska','New Hampshire','New Jersey',
    'New York','Ohio','Oregon','Pennsylvania',
    'Rhode Island','South Carolina','Tennessee','Texas','Utah',
    'Virginia','Washington (state)','West Virginia','Wyoming']

s = {}# can be removed but not going to just yet 



for i in states:
#fin
    
    state = wptools.page(i).get_parse()
    wikstate = wikipedia.page(i)
    summary = wikstate.content
    words = summary.split()

    isIndex = summary.find("is")
    newLineIndex = summary.find("\n")
    shortenedSum = summary[isIndex:newLineIndex]

    #shortsum = re.search("([^(]+)([^r'\s']*)([^\n]*)",summary) FOR ALABAMA
    #shortsum = re.search("([^r'\s']+)([^r'is']*)([^\n]*)",summary) SHOULD WORK BUT DOESNT BUT IT SHOULD


    landarea = state.infobox["TotalAreaUS"]#number as string 

    pop = state.infobox["2010Pop"]

    highestpoint = state.infobox["HighestPoint"]#highest point for example Guadaluple Peak 
    highestpoint = highestpoint[2:len(highestpoint)-2]
    
    highestelev = state.infobox["HighestElevUS"]
    #highestelev = locale.atoi(pop)
    #d = {i:x for i,x in zip(states2,info)}

    if (i == "Georgia (U.S. state)"):
        url = "https://en.wikipedia.org/wiki/" + i + "#/media/File:" + i + "_in_United_States.svg" 
        shortenedSum = "Georgia" + shortenedSum
        i = "Georgia"
    elif i == "Washington (state)":
        url  =  url = "https://en.wikipedia.org/wiki/" + i + "#/media/File:" + i + "_in_United_States.svg" 
        shortenedSum = "Washington" + shortenedSum
        i = "Washington"
    else :
        url = "https://en.wikipedia.org/wiki/" + i + "#/media/File:" + i + "_in_United_States.svg" 
        shortenedSum = i + shortenedSum

    url = url.replace(" ","_")
    
    #s[i] = [landarea,pop,highestelev,url,shortenedSum]
    s = State(i,shortenedSum,landarea,pop,highestelev)
    db.session.add(s)
    
    #print[s]
    #print landarea
    #print pop
    #print highestpoint
    #print highestelev
    #print summary

    """ Unaltered from internet
    ['Alabama','Alaska','American Samoa','Arizona','Arkansas','California','Colorado','Connecticut','Delaware',
    'District of Columbia','Federated States of Micronesia','Florida','Georgia','Guam','Hawaii','Idaho','Illinois',
    'Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Marshall Islands','Maryland','Massachusetts','Michigan',
    'Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico',
    'New York','North Carolina','North Dakota','Northern Mariana Islands','Ohio','Oklahoma','Oregon','Palau','Pennsylvania',
    'Puerto Rico','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virgin Island',
    'Virginia','Washington','West Virginia','Wisconsin','Wyoming']
    """

    """ This is the one with all non states removed 
    ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida',
    'Georgia (U.S. state)','Hawaii','Idaho','Illinois',
    'Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan',
    'Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico',
    'New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania',
    Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont',
    'Virginia','Washington (state)','West Virginia','Wisconsin','Wyoming']
    """

    """ This is the one with all non states + broken states removed ie the one to use 
   ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida',
    'Georgia (U.S. state)','Hawaii','Idaho','Illinois',
    'Indiana','Iowa','Kentucky','Maryland','Massachusetts','Michigan',
    'Mississippi','Missouri','Nebraska','New Hampshire','New Jersey',
    'New York','Ohio','Oregon','Pennsylvania',
    'Rhode Island','South Carolina','Tennessee','Texas','Utah',
    'Virginia','Washington (state)','West Virginia','Wyoming']
    """

    """ Area (sq ft ), Pop, highest point 
    SHITTY STATES
    Kansas - wb - 82,278, 2,911,641, "Mount Sunflower", 4,041
    Lousiana - wb - 50,000, 4,670,724 "Driskill Mountain", 535
    Maine - wb - 35,385, 1,329,328, "Mount Katahdin", 5,270
    Minnesota - wb - 86,939, 5,489,594, "Eagle Mountain" 2,302
    Montana - 147,040, 1,032,949, "Granite Peak" 12,807
    Nevada - wb - 110,653, 2,890,845,"Boundary Peak" 13,147
    New Mexico - wb - 121,589, 2,085,109, "Wheeler Peak" 13,167
    North Carolina - wb - 53,819, 10,042,802, "Mount Mitchell" 6,684 , 
    North Dakota - missing  70,698, 756,927, "White Butte" , 3,508
    Oklahoma - wb - 69,899, 3,911,338, "Black Mesa" , 4,975
    South Dakota - missing  
    78,116, 858,469, "Black Elk Peak", 7,224
    Vermont - wb 
    9616, 626,042, "Mount Mansfield", 4,395 
    Wisconsin - wb 
    65,498, 5,771,337 "Timms Hill" , 1,951

    """



states2 = ["Kansas","Lousiana","Maine","Minnesota","Montana","Nevada","New Mexico",
"North Carolina","North Dakota","Oklahoma","South Dakota","Vermont","Wisconsin"]

for i in states2:
    c = 0
    url = "https://en.wikipedia.org/wiki/" + i + "#/media/File:" + i + "_in_United_States.svg" 
    url = url.replace(" ","_")
    

info = [
 ["82,278", "2,911,641", "Mount Sunflower", "4,041","Kansas is a U.S. state located in the Midwestern United States.[9] Its capital is Topeka and its largest city Wichita. Kansas is named after the Kansa Native American tribe, which inhabited the area.[10] The tribe's name is often said to mean \"people of the wind\" or \"people of the south wind\", although this was probably not the term's original meaning.[11][12] For thousands of years, what is now Kansas was home to numerous and diverse Native American tribes. Tribes in the eastern part of the state generally lived in villages along the river valleys. Tribes in the western part of the state were semi-nomadic and hunted large herds of bison."], 
 ["50,000", "4,670,724", "Driskill Mountain", "535", "Lousiana  is a state located in the southern region of the United States. Louisiana is the 31st most extensive and the 25th most populous of the 50 United States. Its capital is Baton Rouge and largest city is New Orleans. Louisiana is the only state in the U.S. with political subdivisions termed parishes, which are the local government's equivalent to counties. The largest parish by population is East Baton Rouge Parish, and the largest by land area is Plaquemines. Louisiana is bordered by Arkansas to the north, Mississippi to the east, Texas to the west, and the Gulf of Mexico to the south."],
 ["35,385", "1,329,328", "Mount Katahdin", "5,270", "Maine is the northernmost state in the New England region of the northeastern United States. Maine is the 39th most extensive and the 42nd most populous of the 50 U.S. states. It is bordered by New Hampshire to the west, the Atlantic Ocean to the south and east, and the Canadian provinces of New Brunswick and Quebec to the east and north, respectively. Maine is the easternmost state in the contiguous United States, and the northernmost east of the Great Lakes. It is known for its jagged, rocky coastline; low, rolling mountains; heavily forested interior, and picturesque waterways; and also its seafood cuisine, especially clams and lobster. There is a continental climate throughout the state, even in coastal areas such as its most populous city of Portland.[9] The capital is Augusta."],
  ["86,939", "5,489,594", "Eagle Mountain", "2,302", "Minnesota is a state in the Midwestern United States. Minnesota was admitted as the 32nd state on May 11, 1858, created from the eastern half of the Minnesota Territory. The state has a large number of lakes, and is known by the slogan \"Land of 10,000 Lakes\". Its official motto is L'Etoile du Nord (French: Star of the North)."],
 ["147,040", "1,032,949", "Granite Peak", "12,807","Montana is a state in the Western region of the United States. The state's name is derived from the Spanish word montana (mountain). Montana has several nicknames, although none official,[5] including \"Big Sky Country\" and \"The Treasure State\", and slogans that include \"Land of the Shining Mountains\" and more recently \"The Last Best Place\".[6] Montana has a 545-mile (877 km) border with three Canadian provinces: British Columbia, Alberta, and Saskatchewan, the only state to do so.[7][8] It also borders North Dakota and South Dakota to the east, Wyoming to the south, and Idaho to the west and southwest.[7] Montana is ranked 4th in size, but 44th in population and 48th in population density of the 50 United States. The western third of Montana contains numerous mountain ranges. Smaller island ranges are found throughout the state. In total, 77 named ranges are part of the Rocky Mountains. The eastern half of Montana is characterized by western prairie terrain and badlands."],
  ["110,653", "2,890,845","Boundary Peak", "13,1471","Nevada is a is a state in the Western, Mountain West, and Southwestern regions of the United States of America. Nevada is the 7th most extensive, the 35th most populous, and the 9th least densely populated of the 50 United States. Nearly three-quarters of Nevada\'s people live in Clark County, which contains the Las Vegas\u2013Paradise metropolitan area where three of the state\'s four largest incorporated cities are located. Nevada\'s capital is Carson City. Nevada is officially known as the \"Silver State\" due to the importance of silver to its history and economy. It is also known as the \"Battle Born State\", because it achieved statehood during the Civil War (the words \"Battle Born\" also appear on the state flag); as the \"Sage-brush State\", for the native plant of the same name; and as the \"Sage-hen State\". Nevada borders Oregon to the northwest, Idaho to the northeast, California to the west, Arizona to the southeast and Utah to the east."],
    ["121,589", "2,085,109", "Wheeler Peak", "13,167", "New Mexico  is a state located in the southwestern region of the United States of America. It was admitted to the union as the 47th state on January 6, 1912. It is usually considered one of the Mountain States. New Mexico is fifth by area, the 36th-most populous, and the sixth-least densely populated of the 50 United States."], 
  ["53,819", "10,042,802", "Mount Mitchell", "6,684", "North Carolina is a state in the southeastern region of the United States. The state borders South Carolina and Georgia to the south, Tennessee to the west, Virginia to the north, and the Atlantic Ocean to the east. North Carolina is the 28th most extensive and the 9th most populous of the 50 United States. North Carolina is known as the Tar Heel State and the Old North State."],
 ["70,698", "756,927", "White Butte", "3,508", "North Dakota is the 39th state of the United States, having been admitted to the union on November 2, 1889."],
  ["69,899", "3,911,338", "Black Mesa", "4,975", "Oklahoma is a state located in the South Central United States.[11] Oklahoma is the 20th-most extensive and the 28th-most populous of the 50 United States. The state's name is derived from the Choctaw words okla and humma, meaning \"red people\".[12] It is also known informally by its nickname, The Sooner State, in reference to the non-Native settlers who staked their claims on the choicest pieces of land before the official opening date, and the Indian Appropriations Act of 1889, which opened the door for white settlement in America's Indian Territory. The name was settled upon statehood, Oklahoma Territory and Indian Territory were merged and Indian was dropped from the name. On November 16, 1907, Oklahoma became the 46th state to enter the union. Its residents are known as Oklahomans, or informally \"Okies\", and its capital and largest city is Oklahoma City."], 
  ["78,116", "858,469", "Black Elk Peak", "7,224", "South Dakota  is a state located in the Midwestern region of the United States. It is named after the Lakota and Dakota Sioux Native American tribes, who comprise a significant portion of the population and historically dominated the entire territory. South Dakota is the 17th most expansive, but the 5th least populous and the 5th least densely populated of the 50 United States. Once the southern portion of the Dakota Territory, South Dakota became a state on November 2, 1889, simultaneously with North Dakota. Pierre is the state capital and Sioux Falls, with a population of about 171,000, is South Dakota's largest city."], 
  ["9616", "626,042", "Mount Mansfield", "4,395","Vermont is a state in the New England region of the northeastern United States. It borders the other U.S. states of Massachusetts to the south, New Hampshire to the east, New York to the west, and the Canadian province of Quebec to the north. Lake Champlain forms half of Vermont\'s western border with the state of New York and the Green Mountains run north\u2013south the length of the state."],
 ["65,498", "5,771,337", "Timms Hill", "1,951","is a U.S. state located in the north-central United States, in the Midwest and Great Lakes regions. It is bordered by Minnesota to the west, Iowa to the southwest, Illinois to the south, Lake Michigan to the east, Michigan to the northeast, and Lake Superior to the north. Wisconsin is the 23rd largest state by total area and the 20th most populous. The state capital is Madison, and its largest city is Milwaukee, which is located on the western shore of Lake Michigan. The state is divided into 72 counties."],
 ]

c = 0
for i in states2:
    #print(i)
    #print(c)
    url = "https://en.wikipedia.org/wiki/" + i + "#/media/File:" + i + "_in_United_States.svg" 
    url = url.replace(" ","_")
    info[c] += [url]
    #print info[c][4]
    #print info[c][0]
    #print info[c][1]
    #print info[c][2]
    s = State(i,info[c][4],info[c][0],info[c][1],info[c][2])
    db.session.add(s)
    c+=1



d = {i:x for i,x in zip(states2,info)}


#print d 

#z = s.copy()
#z.update(d)

#print z 
db.session.commit()
db.session.close()    

