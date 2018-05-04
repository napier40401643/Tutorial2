import urllib2, json, base64
accesstoken = "UBX52NDZU2F17VA5L4BX"
institution = "10007772"
course = "U56119"
page = 0
url = "http://data.unistats.ac.uk/api/v4/KIS/Institution/{}/Course/{}/FullTime/Statistics.json".format(institution,course)
request = urllib2.Request(url)
request.add_header(
	"Authorization",
	"Basic " + base64.encodestring(accesstoken+":").replace('\n','')
	)
response = urllib2.urlopen(request)
data = json.load(response)
# print json.dumps(data,indent=2)
for c in data:
	if c["Code"] == "SALARY":
		# print (c['Details'])
		for s in c['Details']:
			if s['Code'] == "INSTMED":
				print "The median salary 6 months after graduation for Software Engineering students from Napier is ==> " + s['Code'], s['Value']

for c in data:
	if c["Code"] == "SALARY":
		# print (c['Details'])
		for s in c['Details']:
			if s['Code'] == "LDMED":
				print "The median salary in the sector for software engineering graduates 40 months after graduation is ==> " + s['Code'], s['Value']

for c in data:
	if c["Code"] == "NSS":
		# print (c['Details'])
		for s in c['Details']:
			if s['Code'] == "Q1":
				print "The proportion of software engineering students who agree or strongly agree with the statement Staff are good at explaining things is ==> " + s['Code'], s['Value']
	