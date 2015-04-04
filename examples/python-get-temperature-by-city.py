#!/usr/bin/env python
import sys
import urllib2
import json

# check that a city name has been provided as argument
if len(sys.argv) > 1:
    country = sys.argv[1]
else:
    print 'No city given.'
    exit()

# retrieve weather in the given city
fp = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?units=metric&mode=json&q=' + country)
data = json.load(fp)
fp.close()

# show temperature
print "Temperature in %s: %d" % (country, data['main']['temp'])
