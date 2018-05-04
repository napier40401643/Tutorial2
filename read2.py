import urllib2, json, base64
accesstoken = "UBX52NDZU2F17VA5L4BX"
institution = "10007772"
# institution = "10007849"
# page = 0
# page = 2
page = 4
# page = 0
url = "http://data.unistats.ac.uk/api/v4/KIS/Institution/{}/Courses.json?pageIndex={}".format(institution,page)
request = urllib2.Request(url)
request.add_header("Authorization","Basic " + base64.encodestring(accesstoken+":").replace('\n',''))
response = urllib2.urlopen(request)
data = json.load(response)
for c in data:
	# if c["Title"] == "Computing":
	if c["Title"] == "Software Engineering":
	# if c["Title"] == "Accounting":
		print c['KisCourseId'], c["Title"]
		
