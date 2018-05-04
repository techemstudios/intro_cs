import urllib2
import json
url = urllib2.urlopen('http://api.wunderground.com/api/f52d82a80ed10e46/geolookup/conditions/q/VA/Richmond.json')
json_string = url.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
print("Current temperature in %s is: %s" % (location, temp_f))
url.close()
