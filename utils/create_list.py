#!/usr/bin/env python
import httplib, urllib, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'f157f2833feb46e898122acef0632c23',
}

params = urllib.urlencode({
})

try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    for i in range(1, 6):
	strurl = "/face/v1.0/facelists/star_v" + str(i) + "?%s"
    	conn.request("PUT", strurl % params, "{\"name\": \"faceset_1\"}", headers)
    	response = conn.getresponse()
    	data = response.read()
    	print(data)
    	conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

