#Dave left his suitcase on a bus. Silly Dave! Let's help him get it back.

#download transit data from CTA portal
import urllib
u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data = u.read()
f = open('rt22.xml', 'wb')
f.write(data)
f.close()

##Identify buses traveling northbound of Dave's office
#input cooredinates of Dave's office
latitude = 41.980262
longitude = -87.668452
#parse the document into a tree
from xml.etree.ElementTree import parse
doc = parse('rt22.xml')
#now that we have a nifty "document tree," look through it
candidates = [] #a list to which we'll add all possible buses
for bus in doc.findall('bus'):
    lat = float(bus.findtext('lat'))
    lon = float(bus.findtext('lon'))
    d = bus.findtext('d') #direction of bus
    if lat > latitude and d.startswith("North"): #found one!
        id = bus.findtext('id')
        candidates.append(id) #add it to our list
        
print(candidates)


##Track identified buses until they return to Dave's office
def distance(lat1, lat2):
    return 69*abs(lat1 - lat2)
def monitor():
    u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
    doc = parse(u)
    for bus in doc.findall('bus'):
        busid = bus.findtext('id')
        if busid in candidates:
            lat = float(bus.findtext('lat'))
            dist = distance(latitude, lat) 
            print(busid, dist, 'miles')
    print('-'*10)
import time
while True:
    monitor()
    time.sleep(60)
#I really don't wanna sign up for the static maps API
  #because I think you have to pay for that, so that's all for now
            


#maybe use google static maps API?
#Or maybe CartoDB! Jk, I'll try that on Sunday
# http://evelopers.google.com/maps/documentation/staticmaps/
#to show  in a browser...
#  import webbrowser
#  webbrowser.open('http://...')
