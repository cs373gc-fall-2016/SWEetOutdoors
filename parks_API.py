
import wptools 
#Louisiana, Kansas , Maine, Minnesota, 
"""states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida',
    'Georgia (U.S. state)','Hawaii','Idaho','Illinois',
    'Indiana','Iowa','Kentucky', 'Maryland','Massachusetts','Michigan',
    'Mississippi','Missouri','Nebraska','New Hampshire','New Jersey',
    'New York','Ohio','Oregon','Pennsylvania',
    'Rhode Island','South Carolina','Tennessee','Texas','Utah',
    'Virginia','Washington (state)','West Virginia','Wyoming']"""

s = {}

for i in states:
#do something 

    state = wptools.page(i).get_parse()

    landarea = state.infobox["TotalAreaUS"]#number as string 
    pop = state.infobox["2010Pop"]
    highestpoint = state.infobox["HighestPoint"]#highest point for example Guadaluple Peak 
    highestpoint = highestpoint[2:len(highestpoint)-2]
    highestelev = state.infobox["HighestElevUS"]
    #d = {i:x for i,x in zip(states2,info)}

    # if (i == "Georgia (U.S. state)"):
    #     url = "https://en.wikipedia.org/wiki/" + i + "#/media/File:" + i + "_in_United_States.svg" 
    # elif i == "Washington (state)":
    #     url  = 	url = "https://en.wikipedia.org/wiki/" + i + "#/media/File:" + i + "_in_United_States.svg" 
    # else :
    #     url = "https://en.wikipedia.org/wiki/" + i + "#/media/File:" + i + "_in_United_States.svg" 
    # url = url.replace(" ","_")
    
    s[i] = [landarea,pop,highestelev,url]

    #print[s]
    print (landarea)
    print (pop)
    print (highestpoint)
    print (highestelev)
    

    #Unaltered from internet
    states = ['Alabama','Alaska','American Samoa','Arizona','Arkansas','California','Colorado','Connecticut','Delaware',
    'District of Columbia','Federated States of Micronesia','Florida','Georgia','Guam','Hawaii','Idaho','Illinois',
    'Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Marshall Islands','Maryland','Massachusetts','Michigan',
    'Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico',
    'New York','North Carolina','North Dakota','Northern Mariana Islands','Ohio','Oklahoma','Oregon','Palau','Pennsylvania',
    'Puerto Rico','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virgin Island',
    'Virginia','Washington','West Virginia','Wisconsin','Wyoming']


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
 ["82,278", "2,911,641", "Mount Sunflower", "4,041"], ["50,000", "4,670,724", "Driskill Mountain", "535"],
 ["35,385", "1,329,328", "Mount Katahdin", "5,270"], ["86,939", "5,489,594", "Eagle Mountain", "2,302"],
 ["147,040", "1,032,949", "Granite Peak", "12,807"], ["110,653", "2,890,845","Boundary Peak", "13,1471"],["121,589", "2,085,109", "Wheeler Peak", "13,167"], ["53,819", "10,042,802", "Mount Mitchell", "6,684"],
 ["70,698", "756,927", "White Butte", "3,508"], ["69,899", "3,911,338", "Black Mesa", "4,975"], ["78,116", "858,469", "Black Elk Peak", "7,224"], ["9616", "626,042", "Mount Mansfield", "4,395"],
 ["65,498", "5,771,337", "Timms Hill", "1,951"]
 ]

c = 0
for i in states2:

    url = "https://en.wikipedia.org/wiki/" + i + "#/media/File:" + i + "_in_United_States.svg" 
    url = url.replace(" ","_")
    info[c] += [url]
    c+=1



d = {i:x for i,x in zip(states2,info)}


#print d 

z = s.copy()
z.update(d)

print z 


